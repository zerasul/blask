from pathlib import Path
from os import path

BASE_DIR = Path('.').resolve()

templateDir = path.join(BASE_DIR, "templates")
postDir = path.join(BASE_DIR, "posts")
defaultLayout = "template.html"
staticDir = path.join(BASE_DIR, "static")
title = "blask | A Simple Blog Engine Based on Flask"
errors = {404: "404"}
