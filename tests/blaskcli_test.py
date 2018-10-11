from pytest import fixture
from click.testing import CliRunner
from Blask import blaskcli
from unittest.mock import patch


class TestCLI:

    tempdir = None
    runner = CliRunner()

    def test_init(self):
        with patch('Blask.blaskcli.CLIController.createdir'):
            with patch('Blask.blaskcli.CLIController.createdefaultindexfile'):
                with patch('Blask.blaskcli.CLIController.createsettingsfile'):
                    with patch('Blask.blaskcli.CLIController.createnotfoundpage'):
                        with patch('Blask.blaskcli.CLIController.createdefaulttemplatefile'):
                            run = self.runner.invoke(blaskcli.blaskcli, ['init'])
                            assert "Initializing new Blask Project" in run.output
                            assert 'Now you can execute: blaskcli run' in run.output
