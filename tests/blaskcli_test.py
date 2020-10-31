from click.testing import CliRunner
from blask import blaskcli
from pytest_mock import mocker

class TestCLI:

    tempdir = None
    runner = CliRunner()


    def test_init(self, mocker):
        mocker.patch('os.makedirs')
        mocker.patch('shutil.copy')
        run = self.runner.invoke(blaskcli.blaskcli, ['init'])
        assert "Initializing new blask Project" in run.output
    
    def test_init_with_docker(self, mocker):
        mocker.patch('os.makedirs')
        mocker.patch('shutil.copy')
        run = self.runner.invoke(blaskcli.blaskcli, ['init','--with-docker'])
        assert "Initializing new blask Project" in run.output

    def test_run(self, mocker):
        mocker.patch('blask.blaskcli.blask.run')
        run = self.runner.invoke(blaskcli.blaskcli, ['run'])
        assert "blask (C)" in run.output
