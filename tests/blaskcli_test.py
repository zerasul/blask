from click.testing import CliRunner
from Blask import blaskcli
from pytest_mock import mocker

class TestCLI:

    tempdir = None
    runner = CliRunner()


    def test_init(self, mocker):
            with mocker.patch('os.makedirs'):
                with mocker.patch('__main__.open'):
                    run = self.runner.invoke(blaskcli.blaskcli, ['init'])
                    assert "Initializing new Blask Project" in run.output

