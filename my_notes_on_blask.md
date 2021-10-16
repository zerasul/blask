### Links

* [Hacktoberfest 2021](https://hacktoberfest.digitalocean.com/profile)
* blask repo : https://github.com/zerasul/blask
  * README [blask/README.md at main · zerasul/blask](https://github.com/zerasul/blask/blob/main/README.md) 
* Blask presentation: https://docs.google.com/presentation/d/1GsrSyJ8ps9-ZxBWuxyGNmbfJcGoPed0TsgTxt6zDUao/edit?usp=sharing
* Web del proyecto (Hecha en Blask) : https://getblask.com/ 
  * Examples: [blask | A Simple Blog Engine Based on Flask](https://getblask.com/examples)
* Hub Docker con las imagenes:  https://hub.docker.com/r/zerasul/blask
* issue #32, assigned to me: [Convert from settings.py to an .env file · Issue #32 · zerasul/blask](https://github.com/zerasul/blask/issues/32)
* Two links in Issue #32:
  * https://github.com/pypa/pipenv/blob/master/docs/advanced.rst#-automatic-loading-of-env
  * [The Twelve-Factor App](https://12factor.net/config)
* More on pipenv

  * [pipenv/advanced.rst at master · pypa/pipenv](https://github.com/pypa/pipenv/blob/master/docs/advanced.rst#-automatic-loading-of-env)

* * [Pipenv: Python Dev Workflow for Humans — pipenv 2021.5.29 documentation](https://pipenv.pypa.io/en/latest/)

* More on pyenv
  * [pyenv/pyenv-installer: This tool is used to install `pyenv` and friends.](https://github.com/pyenv/pyenv-installer)
  * [pyenv/pyenv: Simple Python version management](https://github.com/pyenv/pyenv#simple-python-version-management-pyenv)

* dotenv: [python-dotenv: Get and set values in your .env file in local and production servers.](https://github.com/theskumar/python-dotenv)



### Notes

* make pull requests to develop
* See my notes on  Bujo N5 P2xx (Mon 04.10)

### Issue #32 

issue #32: [Convert from settings.py to an .env file · Issue #32 · zerasul/blask](https://github.com/zerasul/blask/issues/32)

`pipenv` reads the `.env` files automatically, [loading the environment variables](https://github.com/pypa/pipenv/blob/master/docs/advanced.rst#-automatic-loading-of-env) that we put into them.

It is a very powerful way to correctly configure an application, following the indications of "[The Twelve-Factor App](https://12factor.net/config)".

An example of a settings.py file converted to an `.env` file could be the following:

```
desarrollo@desarrollo:~/Proyectos/pipenv/blask$ cat .env

# Minimal conf for Blask
FLASK_APP=main.py

# Name of the Template Folder.
templateDir="templates"

# Name of the post Folder
postDir="posts"

# default name of the template file.
defaultLayout="template.html"

# Default name of the static Folder
staticDir="static"

# Title of the blog
tittle="Blask | A Simple Blog Engine Based on Flask"
```

All the environment variables that we want to define, can be included in the `.env` file.

`.gitignore` excludes the` .env` file so that it can not be versioned, so that we can store sensitive data inside it.

A very popular custom is to create a file `.env.example`, with sample data, so that other developers find it very easy to generate their own` .env` file from the `.env.example` file .


