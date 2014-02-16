from rest_framework import serializers

from bookreview.models import (
    Author,
    Book,
)

class AuthorSerializer(serializers.ModelSerializer):
    """
    Interacting with the AuthorSerializer...
    """
    # books = serializers.SerializerMethodField('get_books')

    class Meta:
        model = Author
        fields = ('id', 'first_name', 'last_name')

    # def get_books(self, obj):
    #     books = Book.objects.filter(author=obj)
    #     return [
    #         {
    #             'id': book.id,
    #             'title': book.title,
    #             'isbn': book.isbn,
    #         }
    #         for book in books]


# class BookSerializer(serializers.ModelSerializer):
#     """
#     Interacting with the AuthorSerializer...
#     """
#     title = serializers.Field(source='title')
#     isbn = serializers.Field(source='isbn')
#     author = serializers.SerializerMethodField('get_author')

#     class Meta:
#         model = Book
#         fields = ('id', 'title', 'isbn', 'author')

#     def get_author(self, obj):
#         authors = Author.objects.filter(id=obj.author.id)
#         return [
#             {
#                 'first_name': author.first_name,
#                 'last_name': author.last_name,
#             }
#             for author in authors]
