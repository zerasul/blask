from click.testing import CliRunner
from Blask import blaskcli
from pytest_mock import mocker

class TestCLI:

    tempdir = None
    runner = CliRunner()


    def test_init(self, mocker):
        mocker.patch('os.makedirs')
        mocker.patch('shutil.copy')
        run = self.runner.invoke(blaskcli.blaskcli, ['init'])
        assert "Initializing new Blask Project" in run.output

