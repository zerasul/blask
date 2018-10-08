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


class CLIController:

    default_template_file = '<html><head><title>{{title}}</title></head><body>{{content|safe}}</body>'
    default_index = '# Its Working \n Welcome to Blask'

    def createdefaultindexfile(self, filepath):
        with open(filepath, 'w') as indexfile:
            indexfile.write(self.defaultIndex)

    def createdefaulttemplatefile(self, filepath):
        with open(filepath, 'w') as templatefile:
            templatefile.write(self.default_template_file)

    def createdir(self, dirpath):
        mkdir(dirpath)
        return True


blask = BlaskApp()
isdebug = False
cliController = CLIController()

version = '0.1.0b15'


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
    cliController.createdir(postdir)
    cliController.createdefaultindexfile(path.join(postdir, 'index.md'))
    cliController.createdir(templatedir)
    cliController.createdefaulttemplatefile(path.join(templatedir, 'template.html'))
    click.echo('Created new Blask project on %s' % getcwd())
    click.echo('Now you can execute: blaskcli run')


if __name__ == '__main__':
    blaskcli()








