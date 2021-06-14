from st2tests import fixturesloader

PACK_NAME = "test_content_version"
_, PACK_PATH = fixturesloader.get_fixture_name_and_path(__file__)
PACK_PATH = PACK_PATH[: -len("_fixture")]
