from rest_framework import serializers

from bookreview.models import (
    Author,
    Book,
)

class AuthorSerializer(serializers.ModelSerializer):
    """
    Serializing all the Authors
    """
    books = serializers.SerializerMethodField('get_books')

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name', 'books')

    def get_books(self, obj):
        books = Book.objects.filter(author=obj)
        return [
            {
                'id': book.id,
                'title': book.title,
                'isbn': book.isbn,
            }
            for book in books]
