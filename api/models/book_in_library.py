from django.db import models
from api.models.user import User
from api.models.book import Book


# Create your models here.
class BookInLibrary(models.Model):
    id = models.AutoField(primary_key=True)

    book = models.ManyToManyField(Book, related_name="is_avaiable", blank=False)
    borrowed_by = models.ManyToOneRel(User, blank=True)

    # Metadata
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
