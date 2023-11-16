"""
blask

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
from os import path, listdir
from hashlib import sha3_512
from datetime import datetime

from xml.etree import ElementTree as ET
from werkzeug.utils import safe_join
from werkzeug.exceptions import NotFound
from markdown import Markdown
from typing import List

from blask.errors import PageNotExistError
from blask.blog_entry import BlogEntry

INDEX = "./index.md"
DATE_FORMAT = "%Y-%m-%d"

class BlogRenderer:
    """
    Class BlogRenderer: This class provides the feature for render posts from
    Markdown to HTML and search features.
    :Author: Zerasul <suarez.garcia.victor@gmail.com>
    Date: 2019-05-03
    Version: 0.2.1
    """

    post_dir = None
    """
    Posts Directory
    """
    cache = {}
    """
    Post Cache; improves the post loading.
    """

    def __init__(self, post_dir: str):
        """
        This is the constructor of the blog renderer.
        :param post_dir: Posts Directory. See Settings py for more information.
        """
        self.post_dir = post_dir

    def renderfile(self, filename: str) -> BlogEntry:
        """
        Render a markdown and returns a BlogEntry.
        Note: This method uses a cache based on a SHA-256 hash of the content.
        :param filename: Name of the file without extension.
        :return: BlogEntry.
        :raises PageNotExistError Raise this error if file does not exist or
            would fall out of the posts directory.
        """
        page_not_exist_exception = PageNotExistError(
            f"{filename} does not exists in {self.post_dir} directory")
        try:
            file = f"{filename}.md"
            filepath = safe_join(self.post_dir, file)
        except NotFound:  # file would fall out of given directory
            raise page_not_exist_exception
        try:
            with open(filepath, "r", encoding="utf-8") as content_file:
                content = content_file.read()
                # Check cache
                content_hash = sha3_512(content.encode())
                if content_hash not in self.cache:
                    entry = self.rendertext(filename, content)
                    self.cache[content_hash] = entry
        except FileNotFoundError:
            raise page_not_exist_exception

        return self.cache[content_hash]

    # pylint: disable=R0201
    def rendertext(self, filename: str, text: str) -> BlogEntry:
        """
         Render a Markdown Text and returns the BlogEntry.
        :param filename: filename or title of the post.
        :param text: Text write in Markdown.
        :return: BlogEntry.
        """
        mark_down = Markdown(
            extensions=["meta", "markdown.extensions.codehilite"])
        entry = BlogEntry(filename, mark_down, text)

        return entry

    # pylint: disable=dangerous-default-value
    def list_posts(
            self,
            tags: list = None,
            exclusions: list = [INDEX, "404.md"],
            search: str = "",
            category: str = "",
            author: str = "",
            orderbydate: str = True,
    ) -> List[BlogEntry]:
        """
        Search a list of Posts returning a list of BlogEntry ordered By Date.
        :param tags: list of tags for searching.
        :param exclusions: list of name of posts with exclusions.
        :param search: string with the content what we want of search.
        :param category: list of category of the entry.
        :param author: name of the author of the post
        :param orderbydate: If is set to True the List is Date Inverse Ordered (recent posts first).
        :return: List of BlogEntry.
        """

        files = list(
            filter(
                lambda l: l.endswith(".md") and l not in exclusions,
                self._listdirectoriesrecursive(self.post_dir),
            )
        )
        mapfilter = list(map(lambda l: path.splitext(l)[0], files))
        entries = list(map(lambda l: self.renderfile(l), mapfilter))
        if tags:
            for tag in tags:
                entries = list(filter(lambda l, t=tag: t in l.tags, entries))
        if category:
            entries = list(filter(lambda c: c.category == category, entries))
        if author:
            entries = list(filter(lambda a: a.author == author, entries))
        if search:
            entries = list(filter(lambda l: search in l.content, entries))
        if orderbydate:
            # create a sublist with only entries with date
            datered_entries = list(filter(lambda e: e.date is None, entries))
            not_datered_entries = list(
                filter(lambda d: d.date is not None, entries))
            entries = list(
               sorted(datered_entries, key=lambda t: t.date is not None, reverse=True))
            entries.extend(not_datered_entries)

        return entries

    def _listdirectoriesrecursive(self, directory: str, append: str = "") -> List[str]:
        """
        List the directory and subdirectories
        :param directory: path of the directory where is searching.
        :return: list with all the paths of the files
        """
        posts = []
        for file in listdir(directory):
            if path.isdir(safe_join(directory, file)):
                posts.extend(
                    self._listdirectoriesrecursive(safe_join(directory, file),
                                                   safe_join(append, file))
                )
            else:
                posts.append(safe_join(append, file))
        
        return posts

    def generate_sitemap_xml(self, postlist: str, baseurl: str = "http://localhost:5000"):
        """
        Generate the Sitemap XML format output with all the posts in post_dir
        :param postlist: list with all the posts for the sitemapxml.
        :return: return the xml output for the Sitemap.xml file.
        """
        root = ET.Element(
            "urlset",
            attrib={"xmlns": "http://www.sitemaps.org/schemas/sitemap/0.9"})
        rpostlist = self._listdirectoriesrecursive(postlist)
        rpostlist.remove(INDEX)
        rpostlist = list(map(lambda l: path.splitext(l)[0], rpostlist))
        rpostlist = list(map(lambda l: self.renderfile(l), rpostlist))
        # add index
        urlindex = ET.SubElement(root, "url")
        locindex = ET.SubElement(urlindex, "loc")
        locindex.text = baseurl
        lastmodif = ET.SubElement(urlindex, "lastmod")
        tmp = path.getmtime(path.join(postlist, INDEX))
        lastmodif.text = datetime.fromtimestamp(tmp).strftime(DATE_FORMAT)
        changefreq = ET.SubElement(urlindex, "changefreq")
        changefreq.text = "monthly"
        priority = ET.SubElement(urlindex, "priority")
        priority.text = "0.5"
        for post in rpostlist:
            if post.name:
                title = post.name
            purlindex = ET.SubElement(root, "url")
            plocindex = ET.SubElement(purlindex, "loc")
            plocindex.text = baseurl + title
            plastmodif = ET.SubElement(purlindex, "lastmod")
            filetitle = f"{post.name}.md"
            tmp = path.getmtime(safe_join(self.post_dir, filetitle))
            plastmodif.text = datetime.fromtimestamp(tmp).strftime(DATE_FORMAT)
            pchangefreq = ET.SubElement(purlindex, "changefreq")
            if post.periodicity:
                pchangefreq.text = post.periodicity
            else:
                pchangefreq.text = "monthly"
            priority = ET.SubElement(purlindex, "priority")
            priority.text = "0.5"
        return ET.tostring(root, encoding="UTF-8", method="xml")

    # pylint: disable=R0201
    def generatetagpage(self, post_list: list) -> str:
        """
        Get a HTML with links of the entries.
        :param postlist: List with BlogEntry.
        :return: String with the HTML list.
        """
        content = ""
        
        for post in post_list:
            pname = post.name.replace("\\", "/").replace("./", "")
            entrycontent = f"<li><a href='/{pname}'>{post.name}</a></li>"
            content += entrycontent

        return f"<u>{content}</ul>"

