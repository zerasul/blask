from markdown import Markdown
from os import path
from errors import PageNotExistError


class BlogRenderer:

    postDir = None

    def __init__(self, postdir):
        self.postDir = postdir

    def renderfile(self, filename):
        filepath = path.join(self.postDir, filename+".md")
        if not path.exists(filepath):
            raise PageNotExistError("{} does not exists".format(filename))
        with open(filepath, 'r') as content_file:
            content = content_file.read()
            md = Markdown(['full_yaml_metadata', 'CodeHilite'])
            entry = BlogEntry()
            output = md.convert(content)
            entry.content = output
            if md.Meta is not None:
                entry.date = md.Meta['date']
        return entry
        pass


class BlogEntry:
    content = None
    date = None
    tags = None
