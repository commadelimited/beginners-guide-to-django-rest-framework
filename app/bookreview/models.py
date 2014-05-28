from django.db import models


class AuthorManager(models.Manager):
    pass


class Author(models.Model):
    objects = AuthorManager()
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __unicode__(self):
        return '{} {}'.format(self.first_name, self.last_name)


class BookManager(models.Manager):
    pass


class Book(models.Model):
    objects = BookManager()
    title = models.CharField(max_length=200)
    isbn = models.CharField(max_length=20)
    author = models.ForeignKey(Author, related_name='books')

    def __unicode__(self):
        return self.title
