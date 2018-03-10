from blogrenderer import BlogRenderer
from settings import postDir
from pytest import fixture
from datetime import date


class TestblogRender:

    blogrender = None
    markdowntest = "---\ndate: 2018-03-03\ntags: test,test2\n ---\n test"

    @fixture(autouse=True)
    def initialize(self):
        self.blogrender = BlogRenderer(postDir)

    def test_rendering(self):
        entry = self.blogrender.renderfile("index")
        assert entry.name == "index"


    def test_tagslist(self):
        entries = self.blogrender.list_posts(["blask"])
        assert len(entries) == 1

    def test_rendercontent(self):
        entry = self.blogrender.rendertext("test", self.markdowntest)
        assert entry.name == "test"
        assert entry.date == date(2018, 3, 3)
        assert "test" in entry.tags