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
from os import mkdir, path, getcwd, environ


class CLIController:

    default_template_file = """
    <html>
        <head>
            <title>{{title}}</title>
        </head>
        <body>
            {{content|safe}}
        </body>
    """

    default_index = "# It works!\nWelcome to Blask. Edit `.env` file on your blog's base directory to edit the Blask's settings"

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
        with open(filepath, 'w') as indexfile:
            indexfile.write(self.default_index)

    def createdefaulttemplatefile(self, filepath):
        with open(filepath, 'w') as templatefile:
            templatefile.write(self.default_template_file)

    def createdir(self, dirpath):
            mkdir(dirpath)
            return True

    def createsettingsfile(self):
        with open(path.join(getcwd(), '.env'), 'w') as settingsFile:
            settingsFile.write(self.settings)

    def createnotfoundpage(self, filepath):
        with open(path.join(filepath, '404.md'), 'w') as page:
            page.write(self.not_found)


blask = BlaskApp()
isdebug = False
cliController = CLIController()

version = '0.1.1b1'


@click.group()
@click.option('--debug', default=False)
def blaskcli(debug):
    click.echo('Blask (C) version %s' % version)


@blaskcli.command(help='Run the instance of blask')
def run():
    blask.run(debug=isdebug)


@blaskcli.command(help='Initialize a new Blask Project')
def init():
    click.echo('Initializing new Blask Project')
    click.echo('Using default Settings')
    postdir = blasksettings.DEFAULT_SETTINGS['postDir']
    templatedir = blasksettings.DEFAULT_SETTINGS['templateDir']
    try:
        cliController.createdir(postdir)
        cliController.createdefaultindexfile(path.join(postdir, 'index.md'))
        cliController.createdir(templatedir)
        cliController.createdefaulttemplatefile(path.join(templatedir, 'template.html'))
        cliController.createsettingsfile() # creates a sample settings file
        cliController.createnotfoundpage(postdir) # creates a 404 page
        click.echo('Created new Blask project on %s' % getcwd())
        click.echo('Now you can execute: blaskcli run')
    except FileExistsError:
        click.echo("There is an existing Blask Project")


if __name__ == '__main__':
    blaskcli()
