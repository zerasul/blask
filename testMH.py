from dotenv import dotenv_values
from importlib import import_module
from collections import namedtuple

# TO DO: update dependencies to include dotenv, collections

settings_mod1 = import_module('settings', 'settings')
# this is used in the code, it imports the module, and each variable
# in the module is added as an attribute of the result:
# settings_mod1.vble_name1 = val1, ..., settings_mod1.vble_nameN = valN

print(settings_mod1.defaultLayout)

# This achieves the same from an .env file:

# Step 1) read variables into an OrderedDict as key,value pairs:
settings = dotenv_values(".env.example")
# yields: settings = {'vble_name1':val1 ... 'vble_nameN':'valN'}
# Step 2) convert key, value pairs into attributes of an object:
settings_mod2 = namedtuple("DotEnvSettings",
                           settings.keys())(*settings.values())
# yields: settings_mod2.vble_name1 = val1, ..., settings_mod2.vble_nameN = valN
print(settings_mod2.defaultLayout)
