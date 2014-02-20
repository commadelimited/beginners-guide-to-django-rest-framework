# Beginner's Guide to the Django Rest Framework

So you're learning to use the Django Web Framework and you're loving it. But you want an attractive, easy to use API for your application? Look no further than the [Django Rest Framework](http://www.django-rest-framework.org/) (DRF). The DRF is powerful, sophisticated, and surprisingly easy to use. It offers an attractive web browseable version of your API, and the option of returning raw JSON. The Django Rest Framework allows provides powerful model serialization. Display data using standard function based views, or get granular with powerful class based views for more complex functionality. All in a fully REST compliant wrapper. Let's dig in.

## Laying the foundation

When working with Python applications, it's always a good idea to sandbox your development with a virtual environment. It helps prevent namespace collisions between libraries you need in your application and libraries you might already have installed on your machine, it makes it easy to install dependencies within a virtual env using the `requirements.txt` file, and lastly it makes sharing your development environment with other developers a snap.

Tuts+ has two excellent videos on how to install [virtualenv](http://code.tutsplus.com/articles/python-power-tools-virtualenv--net-31560) and [virtualenvwrapper](http://code.tutsplus.com/articles/python-power-tools-virtualenvwrapper--net-31569). Take a few minutes to walk through those videos to get virtualenv installed on your machine. If you've already got them installed, then skip the next section.

### Setting up your virtual environment

First thing we'll do as part of our application is to set up the virtual environment. Enter the following commands in your Terminal.

```
$ mkvirtualenv drf
$ workon drf
```

It doesn't matter where you are in the file system when these commands are run. All virtualenv files are stored in a centralized location and activated on demand.

### Installing the Django application

Since this article isn't about Django itself, I've saved some time by creating a repository containing the app we'll be working in. It's a simple bookshelf application which will allow us to store lists of authors and books. [Download the companion repository to this article](https://github.com/commadelimited/beginners-guide-to-django-rest-framework), into the directory of your choice, then run `pip install -r requirements.txt` to install all of the dependencies. Remember to make sure you've activated the virtual environment we set up in the last step. After the installation is complete you should be able to type `fab runserver` to start a local web server, and open a web browser pointing to `http://127.0.0.1:8000/`. If you see a list of Authors on screen then you're good to go.

If at any point you're not getting the expected results, please try switching your local repository's branch to to final to see the results, `git checkout final`.

#### Fab? What's that?

Fab == [Fabric](http://docs.fabfile.org/en/1.8/), a [Python task runner](https://gist.github.com/DavidWittman/1886632). From the docs:

> Fabric is a Python (2.5 or higher) library and command-line tool for streamlining the use of SSH for application deployment or systems administration tasks.

While a more complete discussion about Fabric is beyond the scope of this article, I've implemented some basic fab commands which make working with this application a little easier. You've seen the `fab runserver` command. There's also the `fab shell` command which brings up an interactive iPython shell within the context of the application and the `fab syncdb` command which runs Django's syncdb command to sync changes in models to the database.

## Working with Serialization

One powerful feature of the Django Rest Framework is the built in model serialization it offers. With just a few lines of code you can compose powerful representations of your data that can be delivered in a number of formats. As previously mentioned, our application will be a simple bookshelf app, with Authors and Books. I've already created the Author and Book models for you, so open up `/app/bookreview/models.py`. There are already a few Authors stored in the local SQLite database, so let's open up an interactive shell for our app and poke around. Switch to your Terminal window, make sure you're in the `./app` directory and type in the following command.

```
$ fab shell
```

After the shell loads, input the next few lines to retrieve an Author record from the database, which just happens to be mine. What a coincidence. :)

```
$ from bookreview.models import Author
$ author = Author.objects.get(pk=1)
$ author.id
> 1
$ author.first_name
> u'Andy'
$ author.last_name
> u'Matthews'
```

Similarly you can retrieve all of the Author records from the database with a different command:

```
$ from bookreview.models import Author
$ authors = Author.objects.all()
$ authors
> [<Author: Andy Matthews>, <Author: China Mieville>, <Author: Neil Gaiman>, <Author: Veronica Roth>, <Author: Suzanne Collins>, <Author: Brandon Sanderson>, <Author: Rick Riordan>, <Author: Phillip K. Dick>, <Author: John Scalzi>, <Author: Jesse Petersen>]
```
Unfortunately this doesn't return data that an AJAX call can understand. So let's add a serializer for Authors. Close out the shell by typing `quit` and open up `bookreview/serializers.py`. Type, or paste, the next few lines of code and save the file.

```
class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializing all the Authors
    """
    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')
```

Without making any more changes, the serializer gives us quite a bit of power. Head back into the shell and let's review.

```
$ from bookreview.models import Author
$ from bookreview.serializers import AuthorSerializer
$ author = Author.objects.get(pk=1)
$ serialized = AuthorSerializer(author)
$ serialized.data
> {'id': 1, 'first_name': u'Andy', 'last_name': u'Matthews'}
```

Let's add a few more lines of code and see what our API will show us in the browser after our data is run through our new AuthorSerializer. 

### Checking out the web browseable API

First, open `bookreview/urls.py` and add the following line just after the `index_view` route:

```
url(r'^authors/$', views.AuthorView.as_view(), name='author-list'),
```

Next, open `bookreview/views.py` and add these lines to the end of the file:

```
class AuthorView(generics.ListAPIView):
    """
    Returns a list of all authors.
    """
    model = Author
    serializer_class = AuthorSerializer
```

Then make sure to add the import for the AuthorSerializer at the top of the page:

```
from bookreview.serializers import AuthorSerializer
``` 

The default view for Django Rest Framework is the APIView. It allows you to define your own get, put, and delete methods. It's a good way to get base functionality but still have control over the end result. In our case though we're letting the DRF do the heavy lifting for us by extending the ListAPIView. We just need to provide a few bits of information to allow the DRF to connect the pieces. We give it the Author model so that it knows how to talk to the database, and the AuthorSerializer so that the DRF knows how to return the information. We'll only be working with a few of the built in APIViews, but you can [read about all of the options](http://www.django-rest-framework.org/api-guide/generic-views) on the Django Rest Framework website.

Now that you've made those changes, make sure you've got the server running by typing `fab runserver` then enter the URL `http://127.0.0.1:8000/authors/`. You should see an attractively designed API view page containing a list of all the authors in the database; something like this:

![image](images/author_api_view.png =750x)

Now that we've the Authors API view in place, try hitting that URL with a curl command:

```
$ curl http://127.0.0.1:8000/authors/
> [{"id": 1, "first_name": "Andy", "last_name": "Matthews"},..., {"id": 10, "first_name": "Jesse", "last_name": "Petersen"}]
```

Pretty snazzy eh?

### Giving the authors some books!

While this API view is pretty slick, it's a one for one with the database. Let's kick up our API view by composing a more complex data set for Authors, we're going to also include a list of all books as well. Open `bookreview/serializers.py` and add the following line of code immediately after the docstring:

```
books = serializers.SerializerMethodField('get_books')
```

Before we move on, let's examine this line. The serializer is clever...because we indicated which Model it should serialize, it knows everything about that model...properties, lengths, defaults, etc. Notice that we're not defining first_name, last_name, or id directly within the serializer, we're only indicating which fields should be returned to the API in the `fields` property. Try removing first_name from the list, then reload the browser window.

Because the DRF already knows about the properties of the model, it doesn't require us to repeat ourselves. We could just as easily add the following lines to the serializer and the DRF would be just as happy.

```
first_name = serializers.Field(source='first_name')
last_name = serializers.Field(source='last_name')
```

The `serializers.field` method allows you to point to an existing property of the Model, the `source` field, and allows you to explicitly name it something else when returning it to the end user. But what about `serializers.SerializerMethodField`? That allows you to create a custom property, one that's not directly tied to the model, whose content is the result of a method call. In our case, we're going to return an array of books. Let's add that custom method now. Immediately after the `class Meta` definition add the following lines:

```
def get_books(self, obj):
    books = Book.objects.filter(author=obj)
    return [
        {
            'id': book.id,
            'title': book.title,
            'isbn': book.isbn,
        }
        for book in books]
```

Then lastly we need to add our new property, books, to the list of fields. Change this:

```
fields = ('id', 'first_name', 'last_name')
```
to this:

```
fields = ('id', 'first_name', 'last_name', 'books')
```

Reload the `/authors/` endpoint and you should now see an array of books coming in for each author. Not bad for just a few more lines of code eh?

### Adding an Author endpoint

We already have a list of authors, but it would be nice for each author to have their own page...just like MySpace right? Lets add an API endpoint to view a single Author. Open `urls.py` and add the following line after the `author-list` route:

```
url(r'^authors/(?P<pk>[\d]+)/$', views.AuthorInstanceView.as_view(), name='author-instance'),
```

Then open `views.py` and add the following lines after the AuthorView class:

```
class AuthorInstanceView(generics.RetrieveAPIView):
    """
    Returns a single author.
    Also allows updating and deleting
    """
    model = Author
    serializer_class = AuthorSerializer
```

Click one of the Author names on the index page and you should see the Author Instance page load up.

#### Refactoring for the win!

Now would be a good time to do a quick bit of refactoring. Since Django offers the option of naming your routes, we can reference the route by that name. This prevents us from having to build the URL manually. Open `templates/index.html` and swap out the following piece:

```
<a href="/authors/{{author.id}}/">{{author.first_name}} {{author.last_name}}</a>
```

with this line:

```
<a href="{% url 'author-instance' author.id %}">{{author.first_name}} {{author.last_name}}</a>
```

## Saving data. Let the DRF work for you!

Up until now our app has been read only. It's time to start saving some data. Open `templates/index.html` and add the following lines underneath the Authors header:

```
<form action="{% url 'author-list' %}" method="post">
    <input type="text" name="first_name" />
    <input type="text" name="last_name" />
    <input type="submit" value="Add Author" />
</form>
```

Type in a name, yours if you have those sort of ambitions, and hit submit...and presto, you get...an error?

![image](images/405.jpg =500x)

The DRF isn't quite THAT magical...or is it?

Open `views.py`, change the class that AuthorView extends from `generics.ListAPIView` to `generics.ListCreateAPIView`. Then try your request again. Boom! You're an author! And your 4th grade gym teacher said you'd never amount to anything. But what did he know, he has to work around sweaty socks all day. Go back to the main Author's page to see your name in lights.

What just happened? The default API View we used only allowed get requests to the authors endpoint. By changing it to ListCreateAPIView, we told DRF we wanted to also allow POST requests. It does everything else for us. We could just as easily define our own post method within the AuthorView and do some extra stuff there. It might look like this:

```
def post(self, *args, **kwargs):
    import pdb; pdb.set_trace()
```

Keep in mind that while the DRF does enforce database integrity based on the properties of the Model, we're not setting any sort of security on who can access or use this form. Diving into security, logging in, and managing permissions is outside the scope of this article, but suffice it to say that [DRF does have functionality](http://www.django-rest-framework.org/api-guide/permissions) for allowing access to the Views you've been working with, and it's fairly trivial to set up.
