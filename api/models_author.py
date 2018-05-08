from django.db import models
from .models_book import Book

class Author(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,unique=True,blank=False)
    publications = models.ManyToManyField(Book, related_name="authored_by", blank=True)

    # Metadata
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)