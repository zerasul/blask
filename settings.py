import os

BASE_DIR = os.getcwd()

# Templates directory
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')

# Posts directory
POSTS_DIR = os.path.join(BASE_DIR, 'posts')

# Default layout template
DEFAULT_TEMPLATE = "template.html"

# Static files directory
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# Website title
SITE_TITLE = 'Blask | A Simple Blog Engine Based on Flask'
