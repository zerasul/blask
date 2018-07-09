import os
import logging

BASE_DIR = os.getcwd()

DEFAULT_SETTINGS = {
    'templateDir': os.path.join(BASE_DIR, 'templates'),
    'postDir': os.path.join(BASE_DIR, 'posts'),
    'defaultLayout': 'template.html',
    'staticDir': os.path.join(BASE_DIR, 'static'),
    'title': os.path.join(
        BASE_DIR, 'Blask | A Simple Blog Engine Based on Flask')
}


class BlaskSettings(object):
    """
    Blask configuration helper class
    """

    def __init__(self, *args, **kwargs):
        # Check environment variable for settings module
        if 'BLASK_SETTINGS' in os.environ:
            # Load settings from the module in environment variable
            settings_mod = __import__(os.environ['BLASK_SETTINGS'])
            self.settings = {}
            print(dir(settings_mod))
            for key in DEFAULT_SETTINGS.keys():
                value = getattr(settings_mod, key, DEFAULT_SETTINGS[key])
                print(key, value)
                self.settings[key] = value
        else:
            # Copy default settings
            self.settings = DEFAULT_SETTINGS.copy()

        # Keyword arguments always override default and environment settings
        for kw in kwargs.keys():
            if kw in self.DEFAULT_SETTINGS:
                self.settings[kw] = kwargs[kw]

    def __getitem__(self, key):
        """
        Dictionary like settings access
        """
        if key in self.settings:
            return self.settings[key]
        raise KeyError('There is no blask setting called %s' % key)
