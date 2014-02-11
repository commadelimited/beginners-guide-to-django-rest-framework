# Beginner's Guide to the Django Rest Framework

So you're learning to use the Django Web Framework and you're loving it. But you want an attractive, easy to use API for your application? Perhaps one that will automatically deliver content in a number of formats? Look no further than the [Django Rest Framework](http://www.django-rest-framework.org/) (the DRF). The DRF is powerful, sophisticated, and surprisingly easy to use. It features API endpoints that can display either a web view (when hit from your browser), or raw JSON, when hit via an AJAX or curl request. It has built in serialization of models, and allows standard function based views, or powerful class based views for more complex functionality. It's also completely REST compliant 

## Preparing the foundation

When working with Python applications, it's always a good idea to sandbox your development with a virtual environment. That prevents namespace collisions between libraries you need in your application and libraries you might already have installed on your machine. Plus it makes it easy to install dependencies within a virtual env using the `requirements.txt` file. Tuts+ has two excellent videos on how to install [virtualenv](http://code.tutsplus.com/articles/python-power-tools-virtualenv--net-31560) and [virtualenvwrapper](http://code.tutsplus.com/articles/python-power-tools-virtualenvwrapper--net-31569). If you've already got them installed, then move on to the next section.

### Installation

First thing we'll do as part of our application is to set up our virtual environment. Enter the following commands 

```
$ cd <where you want your app>
$ mkvirtualenv drf
$ workon drf
```
Then install Django, and the Django Rest Framework.

```
(drf) $ pip install django
(drf) $ pip install djangorestframework
```

Alternately, you can [fork the repository for this article](http://foo.bar), into the directory of your choice and run `pip install -r requirements.txt`.

### Creating your Django application

Before you can begin working with the Rest Framework you'll need to create a Django application. For this tutorial we'll be creating a list of books on your bookshelf. We'll explore what all that means later, but for now, we need the Django project and app. Enter the following commands into your console.

```
$ django-admin.py startproject bookreview
$ cd bookreview
$ python manage.py startapp bookreview
```

Add `rest_framework` and `books` to `INSTALLED_APPS` within settings.py.




## Your first endpoint

## Writing tests

