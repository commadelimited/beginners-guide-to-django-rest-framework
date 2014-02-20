from django.shortcuts import render
from rest_framework import generics

from bookreview.models import Author

def index_view(request):
    """
    Ensure the user can only see their own profiles.
    """
    response = {
        'authors': Author.objects.all(),
        # 'books': Book.objects.all(),
    }
    return render(request, 'index.html', response)
