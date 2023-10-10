from datetime import datetime

DATE_FORMAT = "%Y-%m-%d"


class BlogEntry:
    """"
    This class has the information about the Blog Posts.
    Author: Zerasul
    Version: 0.0.1.
    """

    content = None
    """Content of the post."""
    date = None
    """Date of post creation"""
    tags = []
    """List of tags of the blog entry."""
    author = None
    """Author of the post"""
    category = None
    """Category of the post"""
    template = None
    """Name of the template file"""
    name = None
    """Name of the post"""
    title = None
    """Title of the Post"""
    periodicity = None
    """Periodicity of the post for sitemap"""

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
        
        if meta:
            if "date" in meta.keys():
                self.date = datetime.strptime(meta["date"][0], DATE_FORMAT)
            if "tags" in meta.keys():
                self.tags = meta["tags"][0].split(",")
            if "template" in meta.keys():
                self.template = meta["template"][0]
            if "category" in meta.keys():
                self.category = meta["category"][0]
            if "author" in meta.keys():
                self.author = meta["author"][0]
            if "title" in meta.keys():
                self.title = meta["title"][0]
            if "periodicity" in meta.keys():
                self.periodicity = meta["periodicity"][0]

    def __str__(self):
        """
        Convert this object to String
        :return: String with the data of this object.
        """
        string = (
            f"['content': {self.content}, 'name': {self.name}, "
            f"'date': {self.date}, 'tags':[{self.tags}], "
            f"'author': {self.author}, 'category': {self.category}, "
            f"'template': {self.template}]"
        )

        return string
