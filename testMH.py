from dotenv import load_dotenv

from importlib import import_module
from pathlib import Path
import os

BASE_DIR = Path(".").resolve()
DEFAULT_SETTINGS = {
    "templateDir": str(BASE_DIR / "templates"),
    "postDir": str(BASE_DIR / "posts"),
    "defaultLayout": str("template.html"),
    "staticDir": str(BASE_DIR / "static"),
    "title": "blask | A Simple Blog Engine Based on Flask",
    "errors": {404: "404"}  # Dictionary with errors handler
}
print("\nDEFAULTS")
for key, value in DEFAULT_SETTINGS.items():
    # value = getattr(key, DEFAULT_SETTINGS)
    print(key, ":", value)

final_settings = DEFAULT_SETTINGS.copy()

# TO DO: update dependencies to include dotenv, collections

settings_mod1 = import_module('settings', 'settings')
# this is used in the code, it imports the module, and each variable
# in the module is added as an attribute of the result:
# settings_mod1.vble_name1 = val1, ..., settings_mod1.vble_nameN = valN

print("\nLoaded from settings.py")
for key in vars(settings_mod1):
    if key in DEFAULT_SETTINGS:
        value = getattr(settings_mod1, key)
        print(key, ":", value)
        final_settings[key] = value

# final settings
print("\nsettings after .py")
for key, value in final_settings.items():
    print(key, ":", value)


"""
# The following achieves something similar from an .env file:

# Step 1) read variables into an OrderedDict as key,value pairs:
settings = dotenv_values(".env")
# yields: settings = {'vble_name1':val1 ... 'vble_nameN':'valN'}
# Step 2) convert key, value pairs into attributes of an object:
settings_mod2 = namedtuple("DotEnvSettings",
                           settings.keys())(*settings.values())
# yields: settings_mod2.vble_name1 = val1, ..., settings_mod2.vble_nameN = valN


for key in settings_mod2._fields:
    if key in DEFAULT_SETTINGS:
        value = getattr(settings_mod2, key)
        print(key, ":", value)
        final_settings[key] = value
"""

print("\n Read from .env")
# remove all environment variables
for key in DEFAULT_SETTINGS:
    if key in os.environ:
        os.environ.pop(key)
# load again from .env
load_dotenv()
# update settings with environment variables
for key in DEFAULT_SETTINGS:
    if key in os.environ:
        value = os.environ[key]
        print(key, ":", value)
        final_settings[key] = value

# final settings
print("\nfinal settings")
for key, value in final_settings.items():
    print(key, ":", value)
