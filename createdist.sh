#!/bin/bash
# Blask Upload Script; create a new module and upload to pypi.
# this script requires python 3.4+ and the next modules:
# - m2r
# - twine
# this script require a valid user and password for upload to Pypi.
rm -R dist
python setup.py sdist bdist_wheel
twine upload dist/Blask-*