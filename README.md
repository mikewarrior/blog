**Welcome to my Blog Repository**

As a first step you will need to install ``python3`` and ``virtualenv`` so install both in your global.

Installing python for a Mac:

```
    brew install python3
```

Installing virtual env just for python3:

```
    pip3 install virtualenv
```

If you come this far, now is time to clone the repository, just run the following command:

```
    git clone https://github.com/mikewarrior/blog
```

Then activate the isolated env for this project:

```
    source path-to-repository/env/blog/bin/activate
```

You should see the isolated env activated in you command line at the beginning of the line something like:

```
    (blog)  your-computer  ~/personal/blogs
```

Finally, we need to install all the python dependencies for the blog project. To able to do this just run:
```
    pip install -r path-to-repository/requirements.txt
```

This will install all the dependencies needed for this project.

Have fun :) adding posts to it!