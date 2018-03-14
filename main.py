from flask import Flask, render_template, request
from blogrenderer import BlogRenderer
from errors import PageNotExistError
import settings

app = Flask(__name__, template_folder=settings.templateDir, static_folder=settings.staticDir)
blogrenderer = BlogRenderer(settings.postDir)


@app.route('/')
def index():
    entry = blogrenderer.renderfile("index")
    template = entry.template
    if template is None:
        template = settings.defaultLayout
    return render_template(template, tittle=settings.tittle, content=entry.content)


@app.route('/search', methods=['POST'])
def searchpages():
    postlist = blogrenderer.list_posts(search=request.form['search'])
    content = blogrenderer.generatetagpage(postlist)
    return render_template(settings.defaultLayout, tittle=settings.tittle, content=content)


@app.route('/tag/<tag>')
def gettag(tag):
    postlist = blogrenderer.list_posts([tag])
    content = blogrenderer.generatetagpage(postlist)
    return render_template(settings.defaultLayout, tittle=settings.tittle, content=content)


@app.route('/<filename>')
def getpage(filename):
    try:
        entry = blogrenderer.renderfile(filename)
    except PageNotExistError:
        entry = blogrenderer.renderfile("404")
    content = entry.content
    date = entry.date
    template = entry.template
    tags = entry.tags
    if template is None:
        template = settings.defaultLayout
    return render_template(template, tittle=settings.tittle, content=content, date=date, tags=tags)
