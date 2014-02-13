from django.db import models


class AuthorManager(models.Manager):
    pass


class Author(models.Model):
    objects = AuthorManager()

    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    @classmethod
    def __str__(self):
        return self.first_name + ' ' + self.last_name