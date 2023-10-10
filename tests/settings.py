import os
from pathlib import Path

BASE_DIR = Path(".").resolve()

# Templates directory
template_dir = os.path.join(BASE_DIR, 'templates')

# Posts directory
post_dir = os.path.join(BASE_DIR, 'posts')

# Default layout template
defaultLayout = "template.html"

# Static files directory
static_dir = os.path.join(BASE_DIR, 'static')

# Website title
title = 'The mantis revenge!'

errors = {
    500: "500",
    404: "404"
}
