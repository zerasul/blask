from pathlib import Path

BASE_DIR = Path(".").resolve()

templateDir = str(BASE_DIR / "templates")
postDir = "posts"
defaultLayout = "template.html"
staticDir = str(BASE_DIR / "static")
theme = "theme_example"
title = "blask | A Simple Blog Engine Based on Flask"
errors = {404: "404"}
