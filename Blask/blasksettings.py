import os

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
        # Copy default settings
        self.settings = DEFAULT_SETTINGS.copy()
        # First of all we check environment
        if 'BLASK_SETTINGS' in os.environ:
            # TODO: Load settings from the path in environment variable
            pass
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
