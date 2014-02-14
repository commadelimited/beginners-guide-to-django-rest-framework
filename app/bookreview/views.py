from django.shortcuts import (
    render,
)

from rest_framework import generics

from bookreview.models import (
    Author,
    Book
)
# from bookreview.serializers import (
#     AuthorSerializer,
# )

def index_view(request):
    """
    Ensure the user can only see their own profiles.
    """
    response = {
        'authors': Author.objects.all(),
        'books': Book.objects.all(),
    }
    return render(request, 'index.html', response)


class AuthorView(generics.ListAPIView):
    """
    Returns a list of all authors.
    """
    model = Author
    # serializer_class = AuthorSerializer


class AuthorInstanceView(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns a single author.
    Also allows updating and deleting
    """
    model = Author
    # serializer_class = AuthorSerializer


class BookView(generics.ListAPIView):
    """
    Returns a list of all books.
    """
    model = Book
    # serializer_class = BookSerializer


class BookInstanceView(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns a single book.
    Also allows updating and deleting
    """
    model = Book
    # serializer_class = BookSerializer
