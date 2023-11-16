"""
blask

Copyright (C) 2018  https://github.com/zerasul/blask

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

import os
from pathlib import Path
from sys import path
from importlib import import_module

BASE_DIR = Path(".").resolve()

DEFAULT_SETTINGS = {
    "template_dir": str(BASE_DIR / "templates"),
    "post_dir": str(BASE_DIR / "posts"),
    "default_layout": str("template.html"),
    "static_dir": str(BASE_DIR / "static"),
    "theme": None,
    "title": "blask | A Simple Blog Engine Based on Flask",
    "errors": {404: "404"}  # Dictionary with errors handler
}


class BlaskSettings():  # pylint: disable=too-few-public-methods
    """
    blask configuration helper class
    """

    def __init__(self, settings: dict):
        """
        Initialize Blask settings module. First, look for the BLASK_SETTINGS environment variable 
        and try to load the module. If BLASK_SETTINGS is not defined try to load the current 
        settings from environment variables (defined in .env) and finally from the default values.
        Settings provided as arguments to the constructor always take precedence.

        :param args:
        :param kwargs:
        """
        # Check environment variable for settings module
        if "BLASK_SETTINGS" in os.environ:
            # add current Dir to Path
            path.append(os.getcwd())

            # Load settings from the module in environment variable
            settings_mod = import_module(
                os.environ["BLASK_SETTINGS"], os.environ["BLASK_SETTINGS"])
            # settings are stored in settings_mod.BASE_DIR,
            # settings_mod.template_dir, etc.

            self.settings = {}
            for key in DEFAULT_SETTINGS:
                # for each of default attributes, try first to read the value
                # in settings_mod and if not defined, use the default
                # Note: settings_mod attributes which are not
                # DEFAULT_SETTINGS are ignored

                value = getattr(settings_mod, key, DEFAULT_SETTINGS[key])
                self.settings[key] = value
        else:
            # Copy default settings
            self.settings = DEFAULT_SETTINGS.copy()

            # replace default settings with environment vars defined in .env
            for key in DEFAULT_SETTINGS:
                if key in os.environ:
                    self.settings[key] = os.environ[key]

        # arguments always override default and environment settings
        for setting in settings:
            if setting in DEFAULT_SETTINGS:
                self.settings[setting] = settings[setting]

        # Set theme
        if self.settings["theme"] != None:
            self.settings["template_dir"] = str(BASE_DIR / "themes" / self.settings['theme'])

    def __getitem__(self, key: str):
        """
        Dictionary like settings access
        """
        if key in self.settings:
            return self.settings[key]
        
        raise KeyError(f"There is no setting named {key}")
