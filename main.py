
from Blask import BlaskApp
import settings

if __name__ == '__main__':
    app = BlaskApp(
        templateDir=settings.TEMPLATE_DIR,
        postDir=settings.POSTS_DIR,
        defaultLayout=settings.DEFAULT_TEMPLATE,
        staticDir=settings.STATIC_DIR,
        tittle=settings.SITE_TITLE)
    app.run()
