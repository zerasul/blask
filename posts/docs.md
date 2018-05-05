# Documentation

In this page we can see all the documentation about the Blask Project:

* [Init Blask](#init-blask)
* [Configure Blask](#configure-blask)
* [Create a Post](#create-post)
* [Post Metadata](#post-metadata)
* [Create a Template](#create-template)
* [Special Pages](#special-pages)
* [Tag Search](#tag-search)
* [Category Search](#category-search)
* [Author Search](#author-search)
* [Search pages](#search-function)

## <a id="init-blask"></a>Init Blask

To init and use Blask you need Python 3.4 or later. you can use `pip` to install Blask.

    pip install blask 
    
or use the source code:

    git clone https://github.com/zerasul/blask/

You also need the following dependencies (Only if you clone the source code):

* Flask
* Markdown
* Markdown-full-yaml-metadata
* Pygments

Theses dependencies can be easily installed using _pip_. Invoke it with the `-r <file>` parameter:

```pip install -r requirements.txt```
 
If you want to run Blask, use the next code to create a standalone app:

    :::python
    from Blask.Blask import Blask
    import settings


    if __name__ == '__main__':
         b = Blask(templateDir=settings.templateDir, postDir=settings.postDir
              , defaultLayout=settings.defaultLayout,staticDir=settings.staticDir, tittle=settings.tittle)
         b.run()

Now you can browse to http://localhost:5000.
  
## <a id="configure-blask"></a>Configure Blask

Blask comes with a settings file with all the configuration of the application; you can see it in the `settings.py` file.

Here is an example:

    :::python
    templateDir = "templates"
    postDir = "posts"
    defaultLayout = "template.html"
    staticDir = "static"
    tittle = "Blask | A Simple Blog Engine Based on Flask"


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
* **category**: Category of the post.
* **author**: Author of the post.

## <a id="create-template"></a>Create a Template

Blask uses _Jinja2_ to render the HTML templates. To create a template, you have to create a new HTML file in templates folder.

Once the file is created, add your HTML and include inside a Jinja2 variable called `content`, which must have the scape modifier.

![example-template](static/img/precodehtml.png)

Also, if you need to show the metadata information you can add some additional variables.

* ```{{date}}```: variable with the post date.
* ```{{tags}}```: variable with the list of tags.
* ```{{category}}```: variable with the category of the post.
* ```{{author}}```: variable with the author of the post.

## <a id="special-pages"></a>Special Pages

With Blask you can edit the content of 2 Special Pages:

* **index page**: This is the main page. Its markdown contents reside in the _index.md_ file in the posts folder.
* **404**: This is the _Page Not Found_ response. Its markdown contents reside in the _404.md_ file in the posts folder.

## <a id="tag-search"></a>Tag Search

With Blask you can search posts by their tags. To see the posts with one particular tag, browse `http://< url >/tag/< tag-name >`.

## <a id="category-search"></a>Category Search

With Blask you can search posts by his category. To see the posts with one particular Category, browse `http://<url>/category/<category-name>`.

## <a id="author-search"></a>Author Search

With Blask you can search by his Author. To see the posts with one particular Author, browse `http://<url>/author/<author-name>`.

## <a id="search-function"></a>Page Search

With Blask you can search by post contents. To do this, just send a POST request to `http://< url >/search` with the `search` parameter set to your search criteria.

