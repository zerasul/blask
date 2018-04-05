from Blask.Blask import Blask
import settings


if __name__ == '__main__':
    b = Blask(templateDir=settings.templateDir, postDir=settings.postDir, defaultLayout=settings.defaultLayout,
              staticDir=settings.staticDir, tittle=settings.tittle)
    b.run()