from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[0]

# Templates directory
templateDir = BASE_DIR / 'templates'

# Posts directory
postDir = BASE_DIR / 'posts'

# Default layout template
defaultLayout = "template.html"

# Static files directory
staticDir = BASE_DIR / 'static'

# Website title
title = 'Blask | A Simple Blog Engine Based on Flask'
