# Documentation

In this page we can see all the documentation about the Blask Project:

* [Init Blask](#init-blask)
* [Configure Blask](#configure-blask)
* [Create a Post](#create-post)
* [Post Metadata](#post-metadata)
* [Create a Template](#create-template)
* [Special Pages](#special-pages)
* [Tag Search](#tag-search)
* [Search pages](#search-function)

## <a id="init-blask"></a>Init Blask

To init and use Blask you need Python 3.4 or later. You also need the following dependencies:

* Flask
* Markdown
* Markdown-full-yaml-metadata
* Pygments

Theses dependencies can be easily installed using _pip_. Invoke it with the `-r <file>` parameter:

```pip install -r requirements.txt```
 
If you want to run Blask, run Flask using `main.py` as the value of the _FLASK_APP_ environment variable:
 
 <pre>
 export FLASK_APP=main.py
 flask run
 </pre>
 
If the `flask` command is not recognised, you can use the python interpreter:
 
```python -m flask run```
 
Now you can browse to http://localhost:5000.
  
## <a id="configure-blask"></a>Configure Blask

Blask comes with a settings file with all the configuration of the application; you can see it in the `settings.py` file.

Here is an example:

<pre>
templateDir = "templates"
postDir = "posts"
defaultLayout = "template.html"
staticDir = "static"
tittle = "Blask | A Simple Blog Engine Based on Flask"
</pre>

Here is the description of each configuration:

* **templateDir**: Templates Folder. All the HTML for the templates must be there.
* **postDir**: Posts Dir. All the markdown blog posts must be there.
* **defaultLayout**: Default template file. This file must be in the _templateDir_ folder.
* **staticDir**: Static resources folder. All the _css_, _js_, _img_ must be here.
* **tittle**: Default title for the site.


## <a id="create-post"></a>Create a Post

Creating a new blog post is very easy with Blask. First you need to create a Markdown file with `.md` extension on the *Posts Folder* 
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

*  The first part is between "---" characters. This is the Metadata part, which contains information about the
post, like the date, the template file that we want to use, or the tags associated with this post.

* The second part is the content of the post; here you can use Markdown to write all the text that you need. If you need 
more information about the Markdown syntax, check the [Markdown Documentation](https://daringfireball.net/projects/markdown/syntax).

## <a id="post-metadata"></a>Post Metadata

Here is the description of the metadata used in posts:

* **date**: Date of the post. Must be in `yyyy-mm-dd` format.
* **template**: Template file for the post. This is the filename and must be in the _templates folder_.
* **tags**: List of tags separated by comma.

## <a id="create-template"></a>Create a Template

Blask uses _Jinja2_ to render the HTML templates. To create a template, you have to create a new HTML file in templates folder.

Once the file is created, add your HTML and include inside a Jinja2 variable called `content`, which must have the scape modifier.

![example-template](static/img/precodehtml.png)

Also, if you need to show the metadata information you can add some additional variables.

+ {{date}}: variable with the post date
* {{tags}}: variable with the list of tags

## <a id="special-pages"></a>Special Pages

With Blask you can edit the content of 2 Special Pages:

* **index page**: This is the main page. Its markdown contents reside in the _index.md_ file in the posts folder.
* **404**: This is the _Page Not Found_ response. Its markdown contents reside in the _404.md_ file in the posts folder.

## <a id="tag-search"></a>Tag Search

With Blask you can search posts by their tags. To see the posts with one particular tag, browse `http://< url >/tag/< tag-name >`.

## <a id="search-function"></a>Page Search

With Blask you can search by post contents. To do this, just send a POST request to `http://< url >/search` with the `search` parameter set to your search criteria.

