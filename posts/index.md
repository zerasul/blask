# Blask

Blask is a blogging engine based on [Flask](http://flask.pocoo.org/), that uses Markdown to show posts. This Microframework grants the possibility to create a blog using only MarkDown and HTML.

Using the Flask Microframework and the [Jinja2](http://jinja.pocoo.org/) template engine, you can easily create a blog with only a few steps.

For Blask to find a new post, all you have to do is write a markdown file and store it in the posts directory.

Example:

    This is an example of *markdown*.

    With this text you can see how _Blask works_.

Once you've written the markdown file, you can view it on your site:

    https://myfancysite.com/hello-world


**Configuration using  _Environment Variables_:**

Before you run the code you have to export the BLASK_SETTINGS enviorement variable.

    :::bash
    export BLASK_SETTINGS=settings

You only need to run the next code:

    :::python
      from blask import BlaskApp
    
      if __name__== '__main__':
          BlaskApp().run() 

**Configuration using  _Blask Command Line Tool_:**

1. Initialize the minimal folders required. This creates the _posts_ and _templates_ directory. 

    ```
    blaskcli init
    ```

2. Run the main code.

    ```
    blaskcli run
    ```

**Note**: This project is in alpha stage; it is not suitable for production environments.

## Documentation

If you want more information about Blask and how to use it, you can check our documentation:

* [Blask Documentation](/docs)
* [Flask Documentation](http://flask.pocoo.org/docs/0.12/)
* [Markdown Documentation](https://daringfireball.net/projects/markdown/syntax)

We also have some [examples](/examples) available.

## Release notes

Here are the release notes of each Blask version:

* [0.2.3](/0.2.3)
* [0.2.2](/0.2.2)
* [0.2.1](/0.2.1)
* [0.2.0](/0.2.0)
* [0.1.4](/0.1.4)
* [0.1.3](/0.1.3)
* [0.1.2](/0.1.2)
* [0.1.1](/0.1.1)
* [0.1.0-beta](/0.1.0-beta)
* [0.0.1-alpha](/0.0.1-alpha)

## Contributing

Blask is Open Source under the [GPL 3.0](https://www.gnu.org/licenses/gpl-3.0.en.html) license. You can see the source code in our [Github repository](https://github.com/zerasul/blask).

You can also see:

* [Authors](https://github.com/zerasul/blask/graphs/contributors)
* [Issue Tracker](https://github.com/zerasul/blask/issues)
