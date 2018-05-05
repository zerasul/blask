# Install

To install Blask, you can use _pip_:

```pip install blask```

Also, you can use git to download the source code:

```git clone https://github.com/zerasul/blask/```

Then, you need to install the dependencies using _pip_:

```pip install -r requirements.txt```

After that, you need to configure Blask, using the _settings.py_ file:

    :::python
    templateDir = "templates"
    postDir = "posts"
    defaultLayout = "template.html"
    staticDir = "static"
    tittle = "Blask"

And finally, you can run the application using this code:

    ::::python
    from Blask.Blask import Blask
    import settings

    if __name__ == '__main__':
        b = Blask(templateDir=settings.templateDir, postDir=settings.postDir
        , defaultLayout=settings.defaultLayout, staticDir=settings.staticDir, tittle=settings.tittle)
        
        b.run()

Now you can browse the main page at http://localhost:5000. If you see the *Blask Home Page*, all is ok and working.
