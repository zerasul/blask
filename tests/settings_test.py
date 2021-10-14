import os
from pathlib import Path
from blask import blasksettings
from blask.blasksettings import BlaskSettings
from pytest import raises


class TestBlaskSettings:
    def test_defaults(self):
        settings = BlaskSettings()
        for kw in blasksettings.DEFAULT_SETTINGS.keys():
            assert settings[kw] == blasksettings.DEFAULT_SETTINGS[kw]

    def test_from_environ(self):
        # changed for new pytest
        os.environ["BLASK_SETTINGS"] = "tests.testsettings"

        settings = BlaskSettings()
        for kw in blasksettings.DEFAULT_SETTINGS.keys():
            if kw == "postDir":
                assert settings[kw] == str(Path(".").resolve() / "posts2")
            elif kw == "title":
                assert settings[kw] == "The mantis revenge!"
            else:
                assert settings[kw] == blasksettings.DEFAULT_SETTINGS[kw]
        del os.environ["BLASK_SETTINGS"]

    def test_kwargs(self):
        kwsettings = {
            "postDir": str(Path.cwd() / "mantispostdir"),
            "title": "The mantis has you!",
        }
        settings = BlaskSettings(**kwsettings)
        for kw in blasksettings.DEFAULT_SETTINGS.keys():
            if kw == "postDir":

                assert settings[kw] == str(Path.cwd() / "mantispostdir")
            elif kw == "title":
                assert settings[kw] == "The mantis has you!"
            else:
                assert settings[kw] == blasksettings.DEFAULT_SETTINGS[kw]

    def test_nokey(self):
        settings = BlaskSettings()
        with raises(KeyError):
            settings["nokey"]
