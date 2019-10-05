"""
Blask

Copyright (C) 2018  https://github.com/zerasul/blask

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program. If not, see <http://www.gnu.org/licenses/>.
"""

from flask import Flask, render_template, request
from Blask.blasksettings import BlaskSettings
from Blask.blogrenderer import BlogRenderer
from Blask.errors import PageNotExistError


class BlaskApp:
    """
    Blask Application Main Class
    :Author: Zerasul <suarez.garcia.victor@gmail.com>
    date: 2018-05-05
    """
    app = None
    blogrenderer = None

    def __init__(self, **kwargs):
        """
        Initialices a new Blask Instance
        :param kwargs: Dictionary with all the required settings; for more info see :settings
        """
        self.settings = BlaskSettings(**kwargs)
        self.blogrenderer = BlogRenderer(self.settings['postDir'])
        self.app = Flask(__name__,
                         template_folder=self.settings['templateDir'],
                         static_folder=self.settings['staticDir'])
        self.app.add_url_rule('/', endpoint='index', view_func=self._index,
                              methods=['GET'])
        self.app.add_url_rule('/<filename>', view_func=self._get_page,
                              methods=['GET'])
        self.app.add_url_rule('/tag/<tag>', view_func=self._get_tag,
                              methods=['GET'])
        self.app.add_url_rule('/search', view_func=self.search_pages,
                              methods=['POST'])
        self.app.add_url_rule('/category/<category>',
                              view_func=self._get_category, methods=['GET'])
        self.app.add_url_rule('/author/<author>', view_func=self._get_author,
                              methods=['GET'])

    def _index(self):
        """
        Render the Index page
        :return: rendered Index Page
        """
        entry = self.blogrenderer.render_file("index")
        template = entry.template
        if template is None:
            template = self.settings['defaultLayout']
        return render_template(template, title=self.settings['title'],
                               content=entry.content)

    def _get_page(self, filename):
        """
        Render a blog post
        :param filename: Name of the Blog Post.
        :return: rendered Blog post or 404 page.
        """
        try:
            entry = self.blogrenderer.render_file(filename)
        except PageNotExistError:
            entry = self.blogrenderer.render_file("404", dir=self.settings['errorDir'])
        content = entry.content
        date = entry.date
        template = entry.template
        tags = entry.tags
        category = entry.category
        author = entry.author
        if template is None:
            template = self.settings['defaultLayout']
        return render_template(template, title=self.settings['title'],
                               content=content, date=date, tags=tags,
                               category=category, author=author)

    def _get_tag(self, tag):
        """
        Render the Tags Page.
        :param tag: Tag for search
        :return: Rendered tags search.
        """
        postlist = self.blogrenderer.list_posts([tag])
        content = self.blogrenderer.generate_tag_page(postlist)
        return render_template(self.settings['defaultLayout'],
                               title=self.settings['title'], content=content)

    def search_pages(self):
        """
        Render the search page. Must Be on Method POST
        :return: rendered search Page
        """
        postlist = self.blogrenderer.list_posts(search=request.form['search'])
        content = self.blogrenderer.generate_tag_page(postlist)
        return render_template(self.settings['defaultLayout'],
                               title=self.settings['title'], content=content)

    def _get_category(self, category):
        """
        Render a category searchpage
        :param category:
        :return: rendered category search page
        """
        postlist = self.blogrenderer.list_posts(category=category)
        content = self.blogrenderer.generate_tag_page(postlist)
        return render_template(self.settings['defaultLayout'],
                               title=self.settings['title'], content=content)

    def _get_author(self, author):
        """
        Render an author searchpage
        :param author: author parameter
        :return:  rendered author search page
        """
        postlist = self.blogrenderer.list_posts(author=author)
        content = self.blogrenderer.generate_tag_page(postlist)
        return render_template(self.settings['defaultLayout'],
                               title=self.settings['title'], content=content)

    def run(self, **kwargs):
        """
        Run the current instance of Blask
        :param kwargs: Dictionary with all the required settings.
        """
        self.app.run(**kwargs)
