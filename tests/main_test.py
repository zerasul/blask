from pytest import fixture
from blask import BlaskApp
import settings


RESPONSE_DATA = b"href='/about'"


class TestMain:

    test_client = None

    @fixture(autouse=True)
    def inittest(self):
        b = BlaskApp(
            templateDir=settings.templateDir,
            postDir=settings.postDir,
            defaultLayout=settings.defaultLayout,
            staticDir=settings.staticDir,
            title=settings.title,
        )
        b.app.testing = True
        b.app.config["SECRET_KEY"] = "supersecretkeyfortesting"
        b.app.config['WTF_CSRF_METHODS'] = []

        self.test_client = b.app.test_client()

    def test_index(self):
        response = self.test_client.get("/")
        assert b"Blask is a blogging engine" in response.data

    def test_page(self):
        response = self.test_client.get("/about")
        assert response.status_code == 200
        assert b"Blask is a simple Blogging engine " in response.data

    def test_nopage(self):
        response = self.test_client.get("/nopageerror")
        assert response.status_code == 200
        assert b"404" in response.data

    def test_search(self):
        response = self.test_client.post("/search", data=dict(search="about"))
        assert response.status_code == 200

    def test_tag_search(self):
        response = self.test_client.get("/tag/about")
        assert response.status_code == 200
        assert RESPONSE_DATA in response.data

    def test_category_search(self):
        response = self.test_client.get("/category/page")
        assert response.status_code == 200
        assert RESPONSE_DATA in response.data

    def test_author_search(self):
        response = self.test_client.get("/author/zerasul")
        assert response.status_code == 200
        assert RESPONSE_DATA in response.data

    def test_sub_page(self):
        response = self.test_client.get("/releases/sub2/test")
        assert response.status_code == 200
        assert b"subdirectory" in response.data

    def test_get_sitemap(self):
        response = self.test_client.get("/sitemap.xml")
        assert response.status_code == 200
        assert b"<url><loc>http://localhost" in response.data
        assert b"/index" not in response.data
