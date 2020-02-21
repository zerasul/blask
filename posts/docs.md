# Documentation

In this page we can see all the documentation about the Blask Project:

* [Init Blask](#init-blask)
* [Configure Blask](#configure-blask)
* [Create a Post](#create-post)
* [Post Metadata](#post-metadata)
* [Create a Template](#create-template)
* [Special Pages](#special-pages)
* [Custom Error Pages](#custom-error-pages)
* [Tag Search](#tag-search)
* [Category Search](#category-search)
* [Author Search](#author-search)
* [Search pages](#search-function)
* [Blask Command Line Tool](#blaskcli)

## <a id="init-blask"></a>Init Blask

To init and use Blask you need **Python 3.4 or later**. you can use `pip` to install Blask.

    pip install blask
    
or use the source code:

    git clone https://github.com/zerasul/blask/

You also need the following dependencies (Only if you clone the source code):

* Flask
* Markdown
* Markdown-full-yaml-metadata
* Pygments

Theses dependencies can be easily installed using _pip_ (Only if you clone the source code). Invoke it with the `-r <file>` parameter:

```pip install -r requirements.txt```
 
If you want to run Blask, use the next code to create a standalone app:

    :::python
    import argparse
    import logging
    from Blask import BlaskApp


    if __name__ == '__main__':
        # Argument parsing
        parser = argparse.ArgumentParser()
        parser.add_argument(
            "-d", "--debug", action='store_true', help="Verbose output")
        parser.add_argument(
        "-v", "--verbose", action='store_true', help="Verbose output")
        args = parser.parse_args()

        if args.debug or args.verbose:
            log = logging.getLogger()
            level = logging.getLevelName('DEBUG')
            log.setLevel(level)
            debug = True
        else:
            debug = False
        BlaskApp().run(debug=debug)
        
There is an alternative for manual running; using the Blask CLI Tool:
 
    :::bash
    blaskcli run
    

**NOTE**: The Blask CLI Tool is only available if you install Blask using setup.py (or using pip).

Now you can browse to http://localhost:5000.
  
## <a id="configure-blask"></a>Configure Blask

Blask needs a settings file with all the configuration of the application; you need to create a `settings.py` file.

Here is an example:

    :::python
    import os

    BASE_DIR = os.getcwd()

    # Templates directory
    templateDir = os.path.join(BASE_DIR, 'templates')

    # Posts directory
    postDir = os.path.join(BASE_DIR, 'posts')

    # Default layout template
    defaultLayout = "template.html"

    # Static files directory
    staticDir = os.path.join(BASE_DIR, 'static')

    # Website title
    title = 'Blask | A Simple Blog Engine Based on Flask'


Here is the description of each configuration:

* **BASE_DIR**: Where is the working directory.
* **templateDir**: Templates Folder. All the HTML for the templates must be there.
* **postDir**: Posts Dir. All the markdown blog posts must be there.
* **defaultLayout**: Default template file. This file must be in the _templateDir_ folder.
* **staticDir**: Static resources folder. All the _css_, _js_, _img_ must be here.
* **title**: Default title for the site.

**Since: 0.10.**

Blask uses the enviorement variable _BLASK_SETTINGS_ to get the entire configuration.

    :::bash
    export BLASK_SETTINGS=settings
    
where ```settings``` have the configuration module of Blask.

If you want to use the default values; you can see then here:

* **TemplatesDir**: _templates_.
* **postDir**: _posts_.
* **defaultLayout**: _template.html_.
* **staticDir**: _static_
* **tittle**: _Blask | A Simple Blog Engine Based on Flask_
     
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

## <a id="custom-error-pages">Custom Error Pages</a>

(**Since 0.1.4**)

With Blask you can set custom error pages for the Http error codes. In the ```settings``` file, you can set the ```errors``` dictionary for link each http error code to the name of the markdown file (without extension), in the post directory.

    :::python
    # settings.py
    ...
    # errors handle dictionary
    errors = { 404 : '404',
            500 : 'mycustom500' 
            }


## <a id="tag-search"></a>Tag Search

With Blask you can search posts by their tags. To see the posts with one particular tag, browse `http://< url >/tag/< tag-name >`.

**Since 0.1.2**: By Default, the list is Date Ordered (Most New First).

## <a id="category-search"></a>Category Search

With Blask you can search posts by his category. To see the posts with one particular Category, browse `http://<url>/category/<category-name>`.

**Since 0.1.2**: By Default, the list is Date Ordered (Most New First).

## <a id="author-search"></a>Author Search

With Blask you can search by his Author. To see the posts with one particular Author, browse `http://<url>/author/<author-name>`.

**Since 0.1.2**: By Default, the list is Date Ordered (Most New First).

## <a id="search-function"></a>Page Search

With Blask you can search by post contents. To do this, just send a POST request to `http://< url >/search` with the `search` parameter set to your search criteria.

**Since 0.1.2**: By Default, the list is Date Ordered (Most New First).

## <a id="blaskcli"></a>Blask Command Line Tool 
**(Since: 0.1.0b12)**

The Blask Command Line Tool, is a program that you can use for control Blask and have some features. For example for create a new Blask project.
For use the Blask CLI Tool, you need to install Blask using the _setup.py_ script ( using pip).

Usage of Blask Command Line Tool:

    :::bash
    Usage: blaskcli [OPTIONS] COMMAND [ARGS]...
    Options:
        --debug
        --help        Show this message and exit.
        --port NUMBER (Only for run command) sets the server listening Port.

    Commands:
        init  Initialize a new Blask Project
        run   Run the instance of blask
        
There are two commands available:

* _init_: creates a new Blask project creating the default folders and minimum files; in the current directory.
* _run_: run a new instance of blask in the current directory. You can set the listening port with _--port_ option.