import os

from Blask import blasksettings
from Blask.blasksettings import BlaskSettings
from pytest import fixture, raises


class TestBlaskSettings:

    def test_defaults(self):
        settings = BlaskSettings()
        for kw in blasksettings.DEFAULT_SETTINGS.keys():
            assert settings[kw] == blasksettings.DEFAULT_SETTINGS[kw]

    def test_from_environ(self):
        os.environ['BLASK_SETTINGS'] = 'testsettings' #changed for the new version of pytest.
        settings = BlaskSettings()
        for kw in blasksettings.DEFAULT_SETTINGS.keys():
            if kw == 'postDir':
                assert settings[kw] == os.path.join(os.getcwd(), 'posts2')
            elif kw == 'title':
                assert settings[kw] == 'The mantis revenge!'
            else:
                assert settings[kw] == blasksettings.DEFAULT_SETTINGS[kw]
        del(os.environ['BLASK_SETTINGS'])

    def test_kwargs(self):
        kwsettings = {
            'postDir': os.path.join(os.getcwd(),'mantispostdir'),
            'title': 'The mantis has you!',
        }
        settings = BlaskSettings(**kwsettings)
        for kw in blasksettings.DEFAULT_SETTINGS.keys():
            if kw == 'postDir':

                assert settings[kw] == os.path.join(
                    os.getcwd(), 'mantispostdir')
            elif kw == 'title':
                assert settings[kw] == 'The mantis has you!'
            else:
                assert settings[kw] == blasksettings.DEFAULT_SETTINGS[kw]

    def test_nokey(self):
        settings = BlaskSettings()
        with raises(KeyError):
            settings['nokey']