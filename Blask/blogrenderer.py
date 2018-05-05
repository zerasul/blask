from markdown import Markdown
from os import path,listdir
from Blask.errors import PageNotExistError


class BlogRenderer:
    """
    Class BlogRenderer: This class provides the feature for render posts from Markdown to HTML and search features.
    :Author: Zerasul <suarez.garcia.victor@gmail.com>
    Date: 2018-05-05
    Version: 0.1.0
    """
    postdir = None
    """
    Posts Directory
    """

    def __init__(self, postdir):
        """
        This is the constructor of the blog renderer.
        :param postdir: Posts Directory. See Settings py for more information.
        """
        self.postdir = postdir

    def renderfile(self, filename):
        """
            Render a markdown and returns the blogEntry.
        :param filename: Number of the file without extension.
        :return: BlogEntry.
        :raises PageNotExistError Raise this error if file does not exists.
        """
        filepath = path.join(self.postdir, filename + ".md")
        if not path.exists(filepath):
            raise PageNotExistError("{} does not exists".format(filename))
        with open(filepath, 'r') as content_file:
            content = content_file.read()
            entry = self.rendertext(filename,content)
        return entry

    def rendertext(self,filename, text):
        """
         Render a Markdown Text and returns the BlogEntry.
        :param filename: filename or title of the post.
        :param text: Text write in Markdown.
        :return: BlogEntry.
        """
        md = Markdown(extensions=['full_yaml_metadata', 'codehilite'])
        entry = BlogEntry(filename, md, text)
        return entry

    def list_posts(self, tags=[], exclusions=["index.md", "404.md"], search="", category="", author=""):
        """
        Search a list of Posts returning a list of BlogEntry.
        :param tags: list of tags for searching.
        :param exclusions: list of name of posts with exclusions.
        :param search: string with the content what we want of search.
        :param category: list of category of the entry.
        :return: List of BlogEntry.
        """
        files = list(filter(lambda l: l.endswith('.md') and l not in exclusions, listdir(self.postdir)))
        mapfilter = list(map(lambda l: path.splitext(l)[0], files))
        entries = list(map(lambda l: self.renderfile(l), mapfilter))
        if tags:
            for tag in tags:
                entries = list(filter(lambda l: tag in l.tags, entries))
        if category:
            entries = list(filter(lambda c: c.category == category, entries))
        if author:
            entries = list(filter(lambda a: a.author == author, entries))
        if search:
            entries = list(filter(lambda l: search in l.content, entries))

        return entries

    def generatetagpage(self, postlist):
        """
        Get a HTML with links of the entries.
        :param postlist: List with BlogEntry.
        :return: String with the HTML list.
        """
        content = '<ul>'
        for post in postlist:
            entrycontent = "<li><a href='/{}'>{}</a></li>".format(post.name, post.name)
            content += entrycontent
        content += "</ul>"
        return content


class BlogEntry:
    """"
    This class has the information about the Blog Posts.
    Author: Zerasul
    Version: 0.0.1.
    """
    content = None
    """Content of the post."""
    date = None
    """ Date of post creation"""
    tags = []
    """List of tags of the blog entry."""
    author = None
    """Author of the post"""
    category = None
    """category of the post"""
    template = None
    """Name of the template file"""
    name = None
    """ Name of the post"""

    def __init__(self, name, md, content):
        """
        Default constructor
        :param name: name of the post
        :param md: Markdown information
        :param content: String with the Content in HTML.
        """
        self.content = md.convert(content)
        self.name = name
        meta = md.Meta
        if meta is not None:
            self.date = meta.get('date')
            self.tags = meta.get('tags').split(",")
            self.template = meta.get('template')
            self.category = meta.get('category')
            self.author = meta.get('author')

    def __str__(self):
        string = "['content': {}, 'name': {}, 'date': {}, 'tags':[{}], 'author': {}, 'category': {}, template': {}]".format(self.content,self.name,self.date,self.tags,self.author,self.category,self.template)
        return string
