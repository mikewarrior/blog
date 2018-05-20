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

**How to start working with BLOG API**

1.- Generate the migrations:

```
    python admin_blog/manage.py makemigrations
```

2.- Apply the migrations:

```
    python admin_blog/manage.py migrate
```

3.- Run the server:

```
    python admin_blog/manage.py runserver
```


This will run the server at ``http://localhost:8000``

**How to query BLOG API**

To query all posts:

```
    curl -X "GET" http://localhost:8000/posts/
```

To query just one element, for example the first post:
```
    curl -X "GET" http://localhost:8000/posts/<post-id>
    Example:
        curl -X "GET" http://localhost:8000/posts/1
```

To add one element:
```
    curl -X "POST" --header "application/json" --data '{"title":"some-title","content":"some-content","author":"some-author"}' http://localhost:8000/posts/create
```

To update an element:

```
    curl -X "PUT" --header "application/json" --data '{"title":"some-title","content":"some-content","author":"some-author"}' http://localhost:8000/posts/<post-id>/edit
```


To delete an element:

```
    curl -X "DELETE" --header "application/json" http://localhost:8000/posts/<post-id>/delete
```

To search by author, content or title:

```
    curl -X "GET" 'http://localhost:8000/posts/?q=<text-to-search|author>'
```