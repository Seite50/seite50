from django.db import models
from api.models.author import Author


# Create your models here.
class Book(models.Model):
    id = models.AutoField(primary_key=True)
    bookid = models.CharField(max_length=255, blank=False, unique=False)
    title = models.CharField(max_length=255, blank=False, unique=False)
    description = models.CharField(max_length=255, blank=True, unique=False)
    published_date = models.DateField(blank=True, unique=False)
    seite50_sentence = models.CharField(
        max_length=4096, blank=True, unique=False)
    authors = models.ManyToManyField(Author, related_name="written_by", blank=True)

    # Metadata
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
