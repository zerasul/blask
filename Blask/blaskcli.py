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
from os import mkdir, path, getcwd

blask = BlaskApp()
isdebug = False

defaultTemplateFile = '<html><head><title>{{title}}</title></head><body>{{content|safe}}</body>'
defaultIndex = '# Its Working \n Welcome to Blask'

@click.group()
@click.option('--debug', default=False)
def blaskcli(debug):
    isdebug = debug
    pass


@blaskcli.command(help='Run the instance of blask')
def run():
    blask.run(debug=isdebug)


@blaskcli.command(help='Initialize a new Blask Project')
def init():
    click.echo('Initializing new Blask Project')
    click.echo('Using default Settings')
    postdir = blasksettings.DEFAULT_SETTINGS['postDir']
    templatedir = blasksettings.DEFAULT_SETTINGS['templateDir']
    static_dir = blasksettings.DEFAULT_SETTINGS['staticDir']
    mkdir(postdir)
    createdefaultindexfile(path.join(postdir, 'index.md'))
    mkdir(templatedir)
    createdefaulttemplatefile(path.join(templatedir, 'template.html'))
    mkdir(static_dir)
    click.echo('Created new Blask project on %s' % getcwd())
    click.echo('Now you can execute: blaskcli run')


def createdefaultindexfile(filepath):
    with open(filepath, 'w') as indexfile:
        indexfile.write(defaultIndex)


def createdefaulttemplatefile(filepath):
    with open(filepath, 'w') as templatefile:
        templatefile.write(defaultTemplateFile)


if __name__ == '__main__':
    blaskcli()








