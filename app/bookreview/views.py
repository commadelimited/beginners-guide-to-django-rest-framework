from django.shortcuts import (
    render,
)

from rest_framework import generics

from bookreview.models import (
    Author
)
from bookreview.serializers import (
    AuthorSerializer,
)

def index_view(request):
    """
    Ensure the user can only see their own profiles.
    """
    response = {
        'authors': Author.objects.all()
    }

    return render(request, 'index.html', response)

class AuthorView(generics.ListAPIView):
    """
    Returns a list of all authors.
    """
    model = Author
    serializer_class = AuthorSerializer

    def get_queryset(self):
        """
        Ensure the user can only see their own profiles.
        """
        qs = Author.objects.filter()

        return qs