from importlib.metadata import version

import fonderie_essai


def test_version_matches_installed_metadata() -> None:
    assert fonderie_essai.__version__ == version("fonderie-essai")
