import os

from st2tests import fixturesloader

__all__ = ["PACK_NAME", "PACK_PATH"]


PACK_NAME = "pack_name_not_the_same_as_dir_name"
PACK_PATH = os.path.join(fixturesloader.get_fixtures_packs_base_path(), PACK_NAME)
