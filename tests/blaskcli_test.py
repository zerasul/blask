from pytest import fixture
from click.testing import CliRunner
from Blask import blaskcli
from tempfile import mkdtemp
from os import chdir, getcwd
from time import time


class TestCLI:

    tempdir = None
    runner = CliRunner()
    originaldir = getcwd()

    @fixture(autouse=True)
    def setup_test(self):
        self.tempdir = mkdtemp(prefix=str(time()))

    def test_init(self):
        chdir(self.tempdir)
        print(getcwd())
        run = self.runner.invoke(blaskcli.blaskcli, ['init'])
        chdir(self.originaldir)
        print(run.output)
        assert "Initializing new Blask Project" in run.output
