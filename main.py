from flask import Flask, render_template, request
from blogrenderer import BlogRenderer
from errors import PageNotExistError
import settings

app = Flask(__name__, template_folder=settings.templateDir, static_folder=settings.staticDir)
blogrenderer = BlogRenderer(settings.postDir)


@app.route('/')
def index():
    """
    Render the Index page
    :return: rendered Index Page
    """
    entry = blogrenderer.renderfile("index")
    template = entry.template
    if template is None:
        template = settings.defaultLayout
    return render_template(template, tittle=settings.tittle, content=entry.content)


@app.route('/search', methods=['POST'])
def searchpages():
    """
    Render the search page. Must Be on Method POST
    :return: rendered search Page
    """
    postlist = blogrenderer.list_posts(search=request.form['search'])
    content = blogrenderer.generatetagpage(postlist)
    return render_template(settings.defaultLayout, tittle=settings.tittle, content=content)


@app.route('/tag/<tag>')
def gettag(tag):
    """
    Render the Tags Page.
    :param tag: Tag for search
    :return: Rendered tags search.
    """
    postlist = blogrenderer.list_posts([tag])
    content = blogrenderer.generatetagpage(postlist)
    return render_template(settings.defaultLayout, tittle=settings.tittle, content=content)


@app.route('/<filename>')
def getpage(filename):
    """
    Render a blog post
    :param filename: Name of the Blog Post.
    :return: rendered Blog post or 404 page.
    """
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
