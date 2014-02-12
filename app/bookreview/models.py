from django.db import models
from django.conf import settings
from django.utils.timezone import now

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    created_at = models.DateTimeField( auto_now_add=True, default=now(), editable=False)
    updated_at = models.DateTimeField( auto_now_add=True, default=now(), editable=False)