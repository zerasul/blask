from pytest import fixture
from click.testing import CliRunner
from Blask import blaskcli
from unittest.mock import patch


class TestCLI:

    tempdir = None
    runner = CliRunner()




    def test_init(self):
        with patch('os.mkdir'):
            with patch('Blask.blaskcli.CLIController.createdefaultindexfile'):
                with patch('Blask.blaskcli.CLIController.createdefaulttemplatefile'):
                    run = self.runner.invoke(blaskcli.blaskcli, ['init'])
                    print(run.output)
                    assert "Initializing new Blask Project" in run.output
