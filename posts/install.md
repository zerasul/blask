#Install

For install Blask, you can use _pip_ for install int:

```pip install blask```

Also, you can use Git for download the source code:

```git clone https://github.com/zerasul/blask/```

Later, need to configure Blask, using _settings.py_.

<pre>
templateDir = "templates"
postDir = "posts"
defaultLayout = "template.html"
staticDir = "static"
tittle = "Blask"
</pre>

Then, need to install the dependencies using _pip_:

```pip install -r requirements.txt```

For last, you can run the application using Flask.

<pre>
FLAS_APP=main.py
flask run
</pre>

**Note**: If ```flask run``` is not recognized as command, you can invoke it using _python_:

 ```python -m flask run```

Now you can browse the main page at http://localhost:5000. If you see Blask Home Page, all is ok and working.
