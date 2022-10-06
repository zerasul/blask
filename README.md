# BLASK

[![blask Build](https://github.com/zerasul/blask/actions/workflows/ci.yml/badge.svg)](https://github.com/zerasul/blask/actions/workflows/ci.yml) [![Coverage Status](https://coveralls.io/repos/github/zerasul/blask/badge.svg?branch=master)](https://coveralls.io/github/zerasul/blask?branch=master) [![sonarcloud-quality-gate](https://sonarcloud.io/api/project_badges/measure?project=blask-project-key&metric=alert_status)](https://sonarcloud.io/dashboard?id=blask-project-key)[![PyPI version](https://badge.fury.io/py/Blask.svg)](https://badge.fury.io/py/Blask) [![Downloads](http://pepy.tech/badge/blask)](http://pepy.tech/count/blask) [![Docker Image Version (tag latest semver)](https://img.shields.io/docker/v/zerasul/blask/0.2.3?color=green&logo=docker)](https://hub.docker.com/r/zerasul/blask) <span class="badge-buymeacoffee"><a href="https://buymeacoffee.com/zerasul" title="Donate to this project using Buy Me A Coffee"><img src="https://img.shields.io/badge/buy%20me%20a%20coffee-donate-yellow.svg" alt="Buy Me A Coffee donate button" /></a></span>

[![Coverage Status](https://coveralls.io/repos/github/zerasul/blask/badge.svg?branch=main)](https://coveralls.io/github/zerasul/blask?branch=main)

Blask is a blogging engine based on [Flask](http://flask.pocoo.org/). Blask uses Markdown syntax to create and render the contents of blog posts.

Blask uses the Jinja2 template engine to render the web templates.

To install Blask, use `pip`:

```shell
pip install blask
```

or download the source code:

```shell
git clone https://github.com/zerasul/blask.git
```

After downloading you need to create a `settings.py` file:

```python
templateDir = "templates"
postDir = "posts"
defaultLayout = "template.html"
staticDir = "static"
title = "Blask | A Simple Blog Engine Based on Flask"
errors= { 404: "404"}
```

You can also use an environment variable to set the settings:

```bash
export BLASK_SETTINGS=settings
```

To Run Blask, use the following Code:

```python
from blask import BlaskApp import settings

if __name__ == '__main__':
    b = BlaskApp(templateDir=settings.templateDir, postDir=settings.postDir, defaultLayout=settings.defaultLayout,
        staticDir=settings.staticDir, title=settings.title, errors={404:'404'})
    b.run()
```

You can use the Blask Command Line Tool to run the site:

```bash
blaskcli run --port 4444 #sets the port to 4444
```

For more information, see the [Blask web page](http://getblask.com/). Also, you can subscribe to our [Mailing List](https://www.freelists.org/archive/blask_mail_list).


## Development with Docker

To use Docker to provide a development environment, make sure you have Docker installed, along with docker-compose of at least version 1.27.

Run this command to start your development environment:

```bash
docker-compose up -d
```

To shut down your development environment, run this command:

```bash
docker-compose down
```

You can access your Blask development site by visiting http://localhost:8000 in your browser.


---

You can see the [Code of Participation](https://www.mozilla.org/en-US/about/governance/policies/participation/) of this project.

Blask is Open Source under the [GPL 3.0](LICENSE) License
