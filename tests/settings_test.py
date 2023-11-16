import os
from pathlib import Path

import pytest
from dotenv import load_dotenv

from blask import blask_settings
from blask.blask_settings import BlaskSettings


class TestBlaskSettings:

    def test_defaults(self):

        # remove all environment variables
        removed_vars = {}
        for key in blask_settings.DEFAULT_SETTINGS:
            if key in os.environ:
                value = os.environ.pop(key)
                removed_vars[key] = value

        settings = BlaskSettings()
        for kw in blask_settings.DEFAULT_SETTINGS.keys():
            assert settings[kw] == blask_settings.DEFAULT_SETTINGS[kw]

        # put environment variables back
        for key, value in removed_vars.items():
            os.environ[key] = value

    def test_from_environ(self):

        # remove all environment variables
        removed_vars = {}
        for key in blask_settings.DEFAULT_SETTINGS:
            if key in os.environ:
                value = os.environ.pop(key)
                removed_vars[key] = value

        # changed for new pytest
        os.environ['BLASK_SETTINGS'] = 'tests.testsettings'

        settings = BlaskSettings()
        for kw in blask_settings.DEFAULT_SETTINGS.keys():
            if kw == 'post_dir':
                assert settings[kw] == str(Path('.').resolve() / 'posts2')
            elif kw == 'title':
                assert settings[kw] == 'The mantis revenge!'
            else:
                assert settings[kw] == blask_settings.DEFAULT_SETTINGS[kw]
        del(os.environ['BLASK_SETTINGS'])

        # put environment variables back
        for key, value in removed_vars.items():
            os.environ[key] = value

    @pytest.mark.skip(reason="Test not working since .env file is not set properly")
    def test_from_dotenv(self):
        # remove all environment variables
        removed_vars = {}
        for key in blask_settings.DEFAULT_SETTINGS:
            if key in os.environ:
                value = os.environ.pop(key)
                removed_vars[key] = value

        # load variables from .env
        load_dotenv()

        # changed for new pytest
        settings = BlaskSettings()
        for kw in blask_settings.DEFAULT_SETTINGS.keys():
            if kw == 'post_dir':
                assert settings[kw] == 'posts-env'
            elif kw == 'title':
                assert settings[kw] == "The mantis with dotenv?!"
            else:
                assert settings[kw] == blask_settings.DEFAULT_SETTINGS[kw]

        # remove all test environment variables
        for key in blask_settings.DEFAULT_SETTINGS:
            if key in os.environ:
                os.environ.pop(key)

        # put original environment variables back
        for key, value in removed_vars.items():
            os.environ[key] = value

    def test_kwargs(self):

        # remove all environment variables
        removed_vars = {}
        for key in blask_settings.DEFAULT_SETTINGS:
            if key in os.environ:
                value = os.environ.pop(key)
                removed_vars[key] = value
        kwsettings = {
            'post_dir': str(Path.cwd() / 'mantispost_dir'),
            'title': 'The mantis has you!',
        }
        settings = BlaskSettings(**kwsettings)

        for kw in blask_settings.DEFAULT_SETTINGS.keys():
            if kw == 'post_dir':
                assert settings[kw] == str(Path.cwd() / 'mantispost_dir')
            elif kw == 'title':
                assert settings[kw] == 'The mantis has you!'
            else:
                assert settings[kw] == blask_settings.DEFAULT_SETTINGS[kw]

        # put original environment variables back
        for key, value in removed_vars.items():
            os.environ[key] = value

    def test_nokey(self):
        settings = BlaskSettings()
        with pytest.raises(KeyError):
            settings['nokey']
