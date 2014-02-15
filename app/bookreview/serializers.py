from rest_framework import serializers

from bookreview.models import (
    Author,
    Book,
)

class AuthorSerializer(serializers.ModelSerializer):
    """
    Interacting with the AuthorSerializer...
    """
    first_name = serializers.Field(source='first_name')
    last_name = serializers.Field(source='last_name')
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


class BookSerializer(serializers.ModelSerializer):
    """
    Interacting with the AuthorSerializer...
    """
    title = serializers.Field(source='title')
    isbn = serializers.Field(source='isbn')
    author = serializers.SerializerMethodField('get_author')

    class Meta:
        model = Book
        fields = ('id', 'title', 'isbn', 'author')

    def get_author(self, obj):
        authors = Author.objects.filter(id=obj.author.id)
        return [
            {
                'first_name': author.first_name,
                'last_name': author.last_name,
            }
            for author in authors]
