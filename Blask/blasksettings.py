"""
Blask

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


BASE_DIR = Path('.').resolve()

DEFAULT_SETTINGS = {
    'templateDir': str(BASE_DIR / 'templates'),
    'postDir': str(BASE_DIR / 'posts'),
    'defaultLayout': str('template.html'),
    'staticDir': str(BASE_DIR / 'static'),
    'title': 'Blask | A Simple Blog Engine Based on Flask'
}


class BlaskSettings(object):
    """
    Blask configuration helper class
    """

    def __init__(self, *args, **kwargs):
        # Check environment variable for settings module
        if 'BLASK_SETTINGS' in os.environ:
            #add current Dir to Path
            path.append(os.getcwd())
            # Load settings from the module in environment variable
            settings_mod = import_module(os.environ['BLASK_SETTINGS'], os.environ['BLASK_SETTINGS'])

            self.settings = {}
            for key in DEFAULT_SETTINGS.keys():
                value = getattr(settings_mod, key, DEFAULT_SETTINGS[key])
                self.settings[key] = value
        else:
            # Copy default settings
            self.settings = DEFAULT_SETTINGS.copy()

        # Keyword arguments always override default and environment settings
        for kw in kwargs.keys():
            if kw in DEFAULT_SETTINGS:
                self.settings[kw] = kwargs[kw]

    def __getitem__(self, key):
        """
        Dictionary like settings access
        """
        if key in self.settings:
            return self.settings[key]
        raise KeyError('There is no blask setting called %s' % key)
