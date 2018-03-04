#Blask

Blask is a Blogging engine based on [Flask](http://flask.pocoo.org/), that use MarkDown to show posts. This MicroFramework grants the posibility of create a blog using only MarkDown and HTML.

Using the MicroFramework Flask and the Template engine [Jinja2](http://jinja.pocoo.org/), you can easily create a Blog with only some steps.

Only you have to do is write a markdown file and store it at the posts directory for Blask Reconigtion.

For example:

<pre>
This is an example of *markdown*.

With this text you can see how _Blask works_.
</pre>

Once you write the markdown file, you can browse to the file url; < site_url >/< filename whitout .md extension >.

If you want to run the application, just use Flask initialization and run it.

<pre>
$ FLASK_APP = main.py
$ flask run
</pre>

**Note**: This project is on alpha version; is not suitable for production enviorements.

## Documentation

If you wants more information about Blask and how to use it, you can browse to our documentation.

* [Blask Documentation](/docs)
* [Flask Documentation](http://flask.pocoo.org/docs/0.12/)
* [Markdown Documentation](https://daringfireball.net/projects/markdown/syntax)

If you need more information about Blask or about their dependencies; you can see our [examples](/examples).

## Change notes

Here is the change notes about all the versions of Blask:

* [0.0.1-alpha](/0.0.1-alpha)

## Contribute

Blask is open Source under the license of [GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html). You can se the source code at our repo on [github](https://github.com/zerasul/blask).

Also, you can see:
* [Authors](/https://github.com/zerasul/blask/graphs/contributors)
* [Issue Tracker](https://github.com/zerasul/blask/issues)








