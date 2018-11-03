import os
from pathlib import Path

#BASE_DIR = os.getcwd()
BASE_DIR = Path(__file__).resolve().parents[0]

# Templates directory
#templateDir = os.path.join(BASE_DIR, 'templates')
templateDir = BASE_DIR / 'templates'

# Posts directory
#postDir = os.path.join(BASE_DIR, 'posts')
postDir = BASE_DIR / 'posts'

# Default layout template
defaultLayout = "template.html"

# Static files directory
#staticDir = os.path.join(BASE_DIR, 'static')
staticDir = BASE_DIR / 'static'

# Website title
title = 'Blask | A Simple Blog Engine Based on Flask'
