## pants plugins

This directory contains StackStorm-specific plugins for pantsbuild.

./pants should be the primary entry point for development related tasks.
This replaces the Makefile and related scripts such that they are more discoverable.
The plugins here add custom goals or other logic into pants.

To see available goals, do "./pants help goals" and "./pants help $goal".

These plugins might be useful outside of the StackStorm project:
- `stevedore_extensions`
- `uses_services`

`uses_services` has some StackStorm-specific assumptions in it, but it might be
generalizable. There are several other StackStorm-specific plugins, but some of
them are only useful in the st2 repo.

These StackStorm-specific plugins might be useful in other StackStorm-related repos.
- `pack_metadata`

These StackStorm-specific plugins are probably only useful for the st2 repo.
- `api_spec`
- `release`
- `sample_conf`
- `schemas`
- `macros.py` (not a plugin - see pants.toml `[GLOBAL].build_file_prelude_globs`)
