"""
Blask

Copyright (C) 2018  https://github.com/zerasul/blask

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""
import click

from Blask import BlaskApp, blasksettings
from os import makedirs, path, getcwd
from pkg_resources import get_distribution, DistributionNotFound


class CLIController:
    """
    Class that controls all the Command Line interface application
    """

    default_template_file = """
<html>
    <head>
        <title>{{title}}</title>

        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <title>Hello Bulma!</title>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bulma/0.7.1/css/bulma.min.css">
        <script defer src="https://use.fontawesome.com/releases/v5.3.1/js/all.js"></script>
        <style>
            h1 {
                font-size: 2em;
            }
        </style>
    </head>
    <body>
        <section class="section">
            <div class="container">
                {{content|safe}}
            </div>
        </section>
    </body>
</html>
"""

    default_index = """# Welcome to Blask!
This is your `index.md` file, located at `posts` directory. Edit this file to add your own index. You can use Markdown to write it!

Blask is currently under development, and we have a lot of things to do.

Wanna help us?

Check [this project at GitHub](https://github.com/zerasul/blask)
"""

    settings = """ 
    # Minimal conf for Blask
    FLASK_APP=main.py                

    # Name of the Template Folder.
    templateDir="templates"

    # Name of the post Folder
    postDir="posts"

    # default name of the template file.
    defaultLayout='template.html'

    # Default name of the static Folder
    staticDir='static'

    # Title of the blog
    title='Blask | A Simple Blog Engine Based on Flask' 
    """

    not_found = "# 404\n Page not found"

    def createdefaultindexfile(self, filepath):
        """
        create a new default index file.
        :param filepath: file path where the new index file is stored
        """
        with open(filepath, "w") as indexfile:
            indexfile.write(self.default_index)

    def createdefaulttemplatefile(self, filepath):
        """
        Create a new default template.
        :param filepath: file path where the new template file is stored.
        """
        with open(filepath, "w") as templatefile:
            templatefile.write(self.default_template_file)

            return True

    def createsettingsfile(self):
        """
        Create a new settings file
        """
        with open(path.join(getcwd(), ".env"), "w") as settingsFile:
            settingsFile.write(self.settings)

    def createnotfoundpage(self, filepath):
        """
        Create a new page not found file.
        :param filepath: file path where the page not found is stored
        """
        with open(path.join(filepath, "404.md"), "w") as page:
            page.write(self.not_found)


blask = BlaskApp()
isdebug = False
cliController = CLIController()


@click.group()
def blaskcli():
    """
    Initialice the command Line Interface Objects.
    """
    try:
        version = get_distribution("Blask").version
    except DistributionNotFound:
        version = "test_version"
    click.echo("Blask (C) version %s" % version)


@blaskcli.command(help="Run the instance of blask")
@click.option("--debug", default=False, help="Init with de debug flag")
@click.option("--port", default=5000, help="Port where the server is listening")
def run(debug, port):
    """
    Run the current blask instance
    :param debug: initialice with debug options
    :param port: port where the port is opened
    """
    blask.run(debug=debug, port=port)


@blaskcli.command(help="Initialize a new Blask Project")
def init():
    """
    Inits a new Blask Instance; with the default options.
    """
    click.echo("Initializing new Blask Project")
    click.echo("Using default Settings")
    postdir = path.basename(path.dirname(str(blasksettings.DEFAULT_SETTINGS["postDir"] + "/")))
    templatedir = path.basename(
        path.dirname(str(blasksettings.DEFAULT_SETTINGS["templateDir"] + "/"))
    )
    try:
        makedirs(postdir)
        cliController.createdefaultindexfile(path.join(postdir, "index.md"))
        makedirs(templatedir)
        cliController.createdefaulttemplatefile(path.join(templatedir, "template.html"))
        cliController.createsettingsfile()  # creates a sample settings file
        cliController.createnotfoundpage(postdir)  # creates a 404 page
        click.echo("Created new Blask project on %s" % getcwd())
        click.echo("Now you can execute: blaskcli run")
    except FileExistsError as e:
        click.echo("There is an existing Blask Project")


if __name__ == "__main__":
    blaskcli()
