from pack_metadata import tailor
from pack_metadata.target_types import PackMetadata, PackMetadataInGitSubmodule


def rules():
    return tailor.rules()


def target_types():
    return [PackMetadata, PackMetadataInGitSubmodule]
