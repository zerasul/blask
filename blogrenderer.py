from markdown import Markdown
from os import path,listdir
from errors import PageNotExistError


class BlogRenderer:

    postdir = None

    def __init__(self, postdir):
        self.postdir = postdir

    def renderfile(self, filename):
        filepath = path.join(self.postdir, filename + ".md")
        if not path.exists(filepath):
            raise PageNotExistError("{} does not exists".format(filename))
        with open(filepath, 'r') as content_file:
            content = content_file.read()
            entry = self.rendertext(filename,content)
        return entry

    def rendertext(self,filename, text):
        md = Markdown(['full_yaml_metadata'])
        entry = BlogEntry(filename, md, text)
        return entry

    def list_posts(self, tags=[], exclusions=["index.md", "404.md"], search=""):
        files = list(filter(lambda l: l.endswith('.md') and l not in exclusions, listdir(self.postdir)))
        mapfilter = list(map(lambda l: path.splitext(l)[0], files))
        entries = list(map(lambda l: self.renderfile(l), mapfilter))
        if tags:
            for tag in tags:
                entries = list(filter(lambda l: tag in l.tags, entries))
        if search:
            entries = list(filter(lambda l: search in l.name, entries))
        return entries

    def generatetagpage(self, postlist):
        content = '<ul>'
        for post in postlist:
            entrycontent = "<li><a href='/{}'>{}</a></li>".format(post.name, post.name)
            content += entrycontent
        content += "</ul>"
        return content


class BlogEntry:
    content = None
    date = None
    tags = []
    template = None
    name = None

    def __init__(self, name, md, content):
        self.content = md.convert(content)
        self.name = name
        meta = md.Meta
        if meta is not None:
            self.date = meta.get('date')
            self.tags = meta.get('tags').split(",")
            self.template = meta.get('template')

    def __str__(self):
        string = "['content': {}, 'name': {}, 'date': {}, tags:[{}], 'template': {}]".format(self.content,self.name,self.date,self.tags,self.template)
        return string
