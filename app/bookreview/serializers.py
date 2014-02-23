from rest_framework import serializers

from bookreview.models import (
    Author,
    Book,
)

class BookSerializer(serializers.ModelSerializer):
    """
    Serializing all the Books
    """

    search_url = serializers.SerializerMethodField('get_search_url')

    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn', 'search_url')

    def get_search_url(self, obj):
        return "http://www.isbnsearch.org/isbn/{}".format(obj.isbn)


class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializing all the Authors
    """
    books = BookSerializer(many=True)

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'books')

