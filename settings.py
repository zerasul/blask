from pathlib import Path
from os import path

BASE_DIR = Path('.').resolve()

template_dir = path.join(BASE_DIR, "templates")
post_dir = path.join(BASE_DIR, "posts")
defaultLayout = "template.html"
static_dir = path.join(BASE_DIR, "static")
theme = "theme_example"
title = "blask | A Simple Blog Engine Based on Flask"
errors = {404: "404"}
