# Install

To install Blask, you can use _pip_:

```pip install blask```

Also, you can use git to download the source code:

```git clone https://github.com/zerasul/blask/```

Then (If you clone the source code), you need to install the dependencies using _pip_:

```pip install -r requirements.txt```

After that, you need to configure Blask, create a file called _settings.py_ file:

    :::python
    templateDir = "templates"
    postDir = "posts"
    defaultLayout = "template.html"
    staticDir = "static"
    title = "Blask"

You can export a environment variable that point to this file:

    :::bash
    export BLASK_SETTINGS=settings
    
You can run the application using this code:

    :::python
    from Blask.Blask import BlaskApp
    import settings

    if __name__ == '__main__':
        b = BlaskApp(templateDir=settings.templateDir, postDir=settings.postDir
        , defaultLayout=settings.defaultLayout, staticDir=settings.staticDir, title=settings.title)
        
        b.run()
If you use the environment Variable you can run Blask without arguments:

    :::python
    from Blask.Blask import BlaskApp
    import settings

    if __name__ == '__main__':
        BlaskApp().run()
        
Or you can use the BlaskCLI tool:
    
    :::bash
    blaskcli run

Now you can browse the main page at http://localhost:5000. If you see the *Blask Home Page*, all is ok and working.
