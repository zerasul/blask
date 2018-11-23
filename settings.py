from pathlib import Path

BASE_DIR = Path('.').resolve()

# Templates directory
templateDir = str(BASE_DIR / 'templates')

# Posts directory
postDir = str(BASE_DIR / 'posts')

# Default layout template
defaultLayout = "template.html"

# Static files directory
staticDir = str(BASE_DIR / 'static')

# Website title
title = 'Blask | A Simple Blog Engine Based on Flask'
