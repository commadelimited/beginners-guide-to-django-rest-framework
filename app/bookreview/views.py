from django.shortcuts import render

from rest_framework import generics

from bookreview.models import Author
from bookreview.serializers import AuthorSerializer

def index_view(request):
    """
    Ensure the user can only see their own profiles.
    """
    response = {
        'authors': Author.objects.all(),
        # 'books': Book.objects.all(),
    }
    return render(request, 'index.html', response)


class AuthorView(generics.ListCreateAPIView):
    """
    Returns a list of all authors.
    """
    model = Author
    serializer_class = AuthorSerializer


class AuthorInstanceView(generics.RetrieveAPIView):
    """
    Returns a single author.
    Also allows updating and deleting
    """
    model = Author
    serializer_class = AuthorSerializer
