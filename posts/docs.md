#Documentation

In this page we can see all the documentation about Blask Project:

* [Init Blask](#init-blask)
* [Configure Blask](#configure-blask)
* [Create a Post](#create-post)
* [Post Metadata](#post-metadata)
* [Create a Template](#create-template)
* [Special Pages](#special-pages)
* [Tag Search](#tag-search)
* [Search pages](#search-function)

##<a id="init-blask"></a>Init Blask

For init and use Blask you need Python 3.4 or later. Also you need the next dependencies:

* Flask
* Markdown
* Markdown-full-yaml-metadata
* Pygments

Theses dependencies can be easy installed using _pip_. Only you need to invoke it with -r <file> paramters:

```pip install -r requirements.txt```
 
 If you want to run Blask, only you need to run Flask using ```main.py``` as _FLASK_APP_ enviorement variable:
 
 <pre>
 export FLASK_APP=main.py
 flask run
 </pre>
 
 If flask command is does not reconiced, you can use python interpreter:
 
 ```python -m flask run```
 
 Now you can browse to http://localhost:5000.
  
##<a id="configure-blask"></a>Configure Blask

Blask comes with a settings file with all the configuration of the application; you can see it on the ```settings.py```file.

Here is an example:

<pre>
templateDir = "templates"
postDir = "posts"
defaultLayout = "template.html"
staticDir = "static"
tittle = "Blask | A Simple Blog Engine Based on Flask"
</pre>

Here is the description of each configuration:

* **templateDir**: Templates Folder. All the html of the templates must be there.
* **postDir**: Posts Dir. All the posts of the blog must be there.
* **defaultLayout**: default template file. This file must be on _templateDir_ folder.
* **staticDir**: Statics resources folder. All the _css_,_js_, _img_ must be here.
* **tittle**: Default title of our web page.


##<a id="create-post"></a>Create a Post

To create a new post is very easy in Blask. First you need to create a empty Markdown file with .md extension on the Posts Folder 
(See configuration). Here is an example:

<pre>

---
date: 2018-04-04
template: template.html
tags: about,blask
---
This is an example of **post** in blask.

With _MarkDown_ you can create easyly great posts.
</pre>

In the previous Markdown text, we can see 2 parts:

*  The first part is between "---" characters. this is the Metadata part. In this part must be the information about the
post, like his date, the template file that we want to use, or the tags associated to this post.

* The second part is the content of the post; here you can use Markdown to write all the text that you need. If you need 
more information about the syntax of Markdown. Check the [Markdown Documentation](https://daringfireball.net/projects/markdown/syntax).

##<a id="post-metadata"></a>Post Metadata

Here is the description of metadata used in posts:

* **date**: Date of the post. Must Have next format yyyy-mm-dd.
* **template**: Template file for the post. This is the filename and must be on _templates folder_.
* **tags**: list of tags separated by comma.

##<a id="create-template"></a>Create a Template

Blask uses _Jinja2_ for render the HTML template. For create a template, you have to create a new HTML file in templates folder.

Once the file is create, put your HTML and put inside a Jinja variablle called ```content``` and must have the scape modifier.

![example-template](static/img/precodehtml.png)

Also, if you need to show the metadata information you can add some variables more.

+ {{date}}: variable with the post variable
* {{tags}}: variable with the list of tags

##<a id="special-pages"></a>Special Pages

In Blask you can edit the content of 2 Special Pages:

* **index page**: This is the main page. Defines the content of this main page; and must be the Markdown assocaited in
the file _index.md; inside the posts Folder.
* **404**: This is the _Page Not Found_ response. Must have the Markdown of this page inside the _404.md_ file, on the posts directory.

##<a id="tag-search"></a>Tag Search

In Blask you can search pages by his tags; for see the pages with one tag asssociated, only you need to browse to http://< url >/tag/< tag-name >.

##<a id="search-function"></a>Page Search

In Blask you can search content in the posts; for do this, only you can to send a POST request to _http://< url >/search_ with the _search_ parameter.

