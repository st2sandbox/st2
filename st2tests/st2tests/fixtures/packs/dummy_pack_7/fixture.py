import os

from st2tests import fixturesloader

__all__ = ["PACK_NAME", "PACK_PATH"]


PACK_NAME = "dummy_pack_7_name"
PACK_PATH = os.path.join(fixturesloader.get_fixtures_packs_base_path(), PACK_NAME)
