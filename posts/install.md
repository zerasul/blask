# Install

To install Blask, you can use _pip_:

```pip install blask```

Also, you can use git to download the source code:

```git clone https://github.com/zerasul/blask/```

After that, you need to configure Blask, using the _settings.py_ file:

<pre>
templateDir = "templates"
postDir = "posts"
defaultLayout = "template.html"
staticDir = "static"
tittle = "Blask"
</pre>

Then, you need to install the dependencies using _pip_:

```pip install -r requirements.txt```

And finally, you can run the application using Flask:

<pre>
FLAS_APP=main.py
flask run
</pre>

**Note**: If `flask run` is not recognized as command, you can invoke it using _python_:

```python -m flask run```

Now you can browse the main page at http://localhost:5000. If you see the *Blask Home Page*, all is ok and working.
