# Beginner's Guide to the Django Rest Framework

So you're learning to use the Django Web Framework and you're loving it. But you want an attractive, easy to use API for your application? Perhaps one that will automatically deliver content in a number of formats? Look no further than the [Django Rest Framework](http://www.django-rest-framework.org/) (the DRF). The DRF is powerful, sophisticated, and surprisingly easy to use.

It offers an attractive web browseable version of your API, and the option of returning raw JSON when hit via an AJAX or curl request. OAuth1 and OAuth2 are baked right in. The framework allows developers to use it's powerful model serialization. Display data using standard function based views, or get granular with powerful class based views for more complex functionality. And of course the Django Rest Framework is fully REST compliant.

## Laying the foundation

When working with Python applications, it's always a good idea to sandbox your development with a virtual environment. That prevents namespace collisions between libraries you need in your application and libraries you might already have installed on your machine. Plus it makes it easy to install dependencies within a virtual env using the `requirements.txt` file. Tuts+ has two excellent videos on how to install [virtualenv](http://code.tutsplus.com/articles/python-power-tools-virtualenv--net-31560) and [virtualenvwrapper](http://code.tutsplus.com/articles/python-power-tools-virtualenvwrapper--net-31569). If you've already got them installed, then move on to the next section.

### Setting up a virtual environment

First thing we'll do as part of our application is to set up our virtual environment. Enter the following commands 

```
$ cd <where you want your app>
$ mkvirtualenv drf
$ workon drf
```

### Installing the Django application

Since this article isn't about Django itself, I've saved some time by creating a repository containing the app we'll be working in. [Download the companion repository to this article](https://github.com/commadelimited/beginners-guide-to-django-rest-framework), into the directory of your choice, then run `pip install -r requirements.txt` to install all of the dependencies. Remember to make sure you've activated the virtual environment we set up in the last step.

After you've taken the steps above, you should be able to type `fab runserver` to start a local web server, and open a web browser pointing to `http://127.0.0.1:8000/`. If you see a list of Authors and Books you're good to go.

#### Fab? What's that?

Fab == [Fabric](http://docs.fabfile.org/en/1.8/), a [Python task runner](https://gist.github.com/DavidWittman/1886632). From the docs:

> Fabric is a Python (2.5 or higher) library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks.

While a more complete discussion about Fabric is beyond the scope of this article, I've implemented some basic fab commands which make working with this application a little easier. You've seen the `fab runserver` command. There's also the `fab shell` command which brings up an interactive iPython shell within the context of the application.

## Your first endpoint



## Writing tests

