from dotenv import dotenv_values, load_dotenv
import os
from importlib import import_module

# TO DO: update dependencies to include dotenv

config = dotenv_values(".env")

print(config)

load_dotenv()

MHTEST2 = os.getenv('MHTEST2')

print(MHTEST2)

MHTEST3 = import_module('settings', 'settings')
# this imports the module, for the variables they are created as attributes:
# MHTEST3.vble_1_name = vble_1_value,
# ...
# MHTEST3.vble_N_name = vble_N_value

print(MHTEST3.BASE_DIR)
