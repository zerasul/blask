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
import logging

BASE_DIR = os.getcwd()

DEFAULT_SETTINGS = {
    'templateDir': os.path.join(BASE_DIR, 'templates'),
    'postDir': os.path.join(BASE_DIR, 'posts'),
    'defaultLayout': 'template.html',
    'staticDir': os.path.join(BASE_DIR, 'static'),
    'title': 'Blask | A Simple Blog Engine Based on Flask'
}


class BlaskSettings(object):
    """
    Blask configuration helper class
    """

    def __init__(self, *args, **kwargs):
        # Check environment variable for settings module
        if 'BLASK_SETTINGS' in os.environ:
            # Load settings from the module in environment variable
            settings_mod = __import__(
                os.environ['BLASK_SETTINGS'],
                globals(),
                locals(),
                ['object'],
                0)
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
