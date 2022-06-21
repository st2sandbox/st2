# Copyright 2021 The StackStorm Authors.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
from collections import defaultdict
from dataclasses import dataclass
from typing import List, Tuple

from pants.backend.python.goals.setup_py import SetupKwargsRequest
from pants.base.specs import AddressSpecs, SiblingAddresses
from pants.engine.addresses import Address
from pants.engine.rules import collect_rules, Get, MultiGet, rule
from pants.engine.target import Targets
from pants.util.frozendict import FrozenDict
from pants.util.logging import LogLevel

from stevedore_extensions.target_types import (
    ResolvedStevedoreEntryPoints,
    ResolveStevedoreEntryPointsRequest,
    StevedoreEntryPoints,
    StevedoreEntryPointsField,
    StevedoreExtension,
    StevedoreNamespaceField,
)


@dataclass(frozen=True)
class StevedoreSetupKwargs:
    """
    kwargs = {"entry_points": {"stevedore.extension.namespace": ("entry = p.o.i.n:t")}
    """

    kwargs: FrozenDict[str, FrozenDict[str, Tuple[str]]]


@dataclass(frozen=True)
class StevedoreSetupKwargsRequest:
    """Light wrapper around SetupKwargsRequest to allow composed Kwargs."""

    request: SetupKwargsRequest


@rule(
    desc="Prepare stevedore_extension kwargs (entry_points) for usage in setup.py.",
    level=LogLevel.DEBUG,
)
async def stevedore_kwargs_for_setup_py(
    stevedore_request: StevedoreSetupKwargsRequest,
) -> StevedoreSetupKwargs:
    """
    Only one plugin can provide Kwargs for a given setup, so that repo-specific
    plugin's setup_py rule should do something like this:

    custom_args = {...}
    stevedore_kwargs = await Get(StevedoreSetupKwargs, StevedoreSetupKwargsRequest(request))
    return SetupKwargs(
        **request.explicit_kwargs,
        **stevedore_kwargs.kwargs,
        **custom_args,
        address=address
    )
    """

    request: SetupKwargsRequest = stevedore_request.request
    address: Address = request.target.address

    sibling_targets = await Get(
        Targets, AddressSpecs([SiblingAddresses(address.spec_path)])
    )
    stevedore_targets: List[StevedoreExtension] = [
        tgt for tgt in sibling_targets if tgt.has_field(StevedoreEntryPointsField)
    ]
    resolved_entry_points: Tuple[ResolvedStevedoreEntryPoints, ...] = await MultiGet(
        Get(
            ResolvedStevedoreEntryPoints,
            ResolveStevedoreEntryPointsRequest(tgt[StevedoreEntryPointsField]),
        )
        for tgt in stevedore_targets
    )

    entry_points_kwargs = defaultdict(list)
    for target, resolved_ep in zip(stevedore_targets, resolved_entry_points):
        namespace: StevedoreNamespaceField = target[StevedoreNamespaceField]
        entry_points: StevedoreEntryPoints = resolved_ep.val

        for entry_point in entry_points:
            entry_points_kwargs[namespace.value].append(
                f"{entry_point.name} = {entry_point.value.spec}"
            )
    return StevedoreSetupKwargs(
        FrozenDict(
            {
                "entry_points": FrozenDict(
                    (k, tuple(v)) for k, v in sorted(entry_points_kwargs.items())
                )
            }
        )
    )


def rules():
    return collect_rules()
