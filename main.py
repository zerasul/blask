from flask import Flask, render_template
from blogrenderer import BlogRenderer
from errors import PageNotExistError
import settings

app = Flask(__name__, template_folder=settings.templateDir, static_folder=settings.staticDir)
blogrenderer = BlogRenderer(settings.postDir)


@app.route('/')
def index():
    content = blogrenderer.renderfile("index")
    return render_template(settings.defaultLayout, tittle=settings.tittle, content=content.content)

#@app.route('/tag/<tag>')
#def gettag(tag):


@app.route('/<filename>')
def getpage(filename):
    try:
        entry = blogrenderer.renderfile(filename)
    except PageNotExistError:
        entry = blogrenderer.renderfile("404")
    content = entry.content
    date = entry.date
    return render_template(settings.defaultLayout, tittle=settings.tittle, content=content, date=date)