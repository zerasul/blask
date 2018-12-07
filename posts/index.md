# Blask

Blask is a blogging engine based on [Flask](http://flask.pocoo.org/), that uses MarkDown to show posts. This MicroFramework grants the possibility to create a blog using only MarkDown and HTML.

Using the Flask MicroFramework and the [Jinja2](http://jinja.pocoo.org/) template engine, you can easily create a blog with only a few steps.

For Blask to find a new post, all you have to do is write a markdown file and store it in the posts directory.

Example:

    This is an example of *markdown*.

    With this text you can see how _Blask works_.

Once you've written the markdown file, you can view it on your site:

    https://myfancysite.com/hello-world

Before you run the code you have to export the BLASK_SETTINGS enviorement variable.

    :::bash
    export BLASK_SETTINGS=settings


Only you need to run the next code:

    :::python
      from Blask import BlaskApp
    
      if __name__== '__main__':
          BlaskApp().run() 

Or You can use the _Blask Command Line Tool_:

    :::bash
    blaskcli run

**Note**: This project is in alpha stage; it is not suitable for production environments.

## Documentation

If you want more information about Blask and how to use it, you can check our documentation:

* [Blask Documentation](/docs)
* [Flask Documentation](http://flask.pocoo.org/docs/0.12/)
* [Markdown Documentation](https://daringfireball.net/projects/markdown/syntax)

We also have some [examples](/examples) available.

## Release notes

Here are the release notes of each Blask version:

* [0.1.1](/0.1.1)
* [0.1.0-beta](/0.1.0-beta)
* [0.0.1-alpha](/0.0.1-alpha)

## Contributing

Blask is Open Source under the [GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) license. You can see the source code in our [Github repository](https://github.com/zerasul/blask).

Also, you can see:

* [Authors](https://github.com/zerasul/blask/graphs/contributors)
* [Issue Tracker](https://github.com/zerasul/blask/issues)








