#Examples

In this page, you can see some examples of use for Blask. From create our first post, until create templates.

## Configure and Run Blask

First if you need to run Blask, need to see the ```settings.py``` file and set the properly configuration.

<pre>
templateDir = "templates" # The templates Folder.
postDir = "posts" # The posts Folder (markdown Files).
defaultLayout = "template.html" # Default template file. Must be in Templates Folder.
staticDir = "static" # The static Folder (css,js,img...).
tittle = "Blask" (Title of the web Page).
</pre>

Once You set the configuration, run the next steps on terminal.

<pre>
$ FLASK_APP=main.py #must be on blask directory.
$ flask run
</pre>

Then browse to http://localhost:5000 and see the Blask Home Page. Of course you can modify the markdown, and see how it changes.

## Create first post

For create a new post, only need to do is create a new markdown file in the posts Directory. For Example:

File: newpost.md

<pre>

---
date: 2018-04-04
template: template.html
tags: blask,test
---
This is an example of **MarkDown**. This is a test _web page_.
</pre>

Once we save the previous file, we can browse to http://localhost:5000/newpost and see the result.

## Create Template

To create a new Template, only you have to do is create a new HTML file in the templates folder, and inside the HTML code
include the jinja2 Template ```content```. Here is an example:


![precode-html](static/img/precodehtml.png)

Once you create a new template, you can reference to it in two ways:

* First, using the default template setting in the ```settings.py``` file.

* Second, using the metadata space of the Markdown Documents.
