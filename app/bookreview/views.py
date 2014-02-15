from django.shortcuts import (
    render,
)

from rest_framework import generics

from bookreview.models import (
    Author,
    Book
)
from bookreview.serializers import (
    AuthorSerializer,
    BookSerializer,
)

def index_view(request):
    """
    Ensure the user can only see their own profiles.
    """
    response = {
        'authors': Author.objects.all(),
        'books': Book.objects.all(),
    }

    # @csrf_exempt
    # def snippet_list(request):
    #     """
    #     List all code snippets, or create a new snippet.
    #     """
    #     if request.method == 'GET':
    #         snippets = Snippet.objects.all()
    #         serializer = SnippetSerializer(snippets, many=True)
    #         return JSONResponse(serializer.data)

    #     elif request.method == 'POST':
    #         data = JSONParser().parse(request)
    #         serializer = SnippetSerializer(data=data)
    #         if serializer.is_valid():
    #             serializer.save()
    #             return JSONResponse(serializer.data, status=201)
    #         return JSONResponse(serializer.errors, status=400)

    return render(request, 'index.html', response)


class AuthorView(generics.ListAPIView):
    """
    Returns a list of all authors.
    """
    model = Author
    serializer_class = AuthorSerializer
    # serializer_class = AuthorSerializer


class AuthorInstanceView(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns a single author.
    Also allows updating and deleting
    """
    model = Author
    serializer_class = AuthorSerializer

    # serializer_class = AuthorSerializer


class BookView(generics.ListAPIView):
    """
    Returns a list of all books.
    """
    model = Book
    serializer_class = BookSerializer


class BookInstanceView(generics.RetrieveUpdateDestroyAPIView):
    """
    Returns a single book.
    Also allows updating and deleting
    """
    model = Book
    serializer_class = BookSerializer
