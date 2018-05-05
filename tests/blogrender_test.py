from Blask.blogrenderer import BlogRenderer
from settings import postDir
from pytest import fixture, raises
from datetime import date
from Blask.errors import PageNotExistError


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

    def test_pagenotexists(self):
        with raises(PageNotExistError):
            self.blogrender.renderfile("notexists")

    def test_generatetag(self):
        entries = self.blogrender.list_posts(["about"])
        taglist = self.blogrender.generatetagpage(entries)
        assert "href='/about'" in taglist

    def test_categorylist(self):
        entries = self.blogrender.list_posts(category="page")
        assert len(entries) == 1

    def test_authorlist(self):
        entries = self.blogrender.list_posts(author="zerasul")
        assert len(entries) == 1

    def test_search(self):
        entries = self.blogrender.list_posts(search='documentation')
        assert len(entries) == 1
        entrieslist = self.blogrender.generatetagpage(entries)
        assert "href='/docs'" in entrieslist
