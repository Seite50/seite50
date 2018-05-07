from django.db import models

# Create your models here.
class Book(models.Model):
    id = models.CharField(max_length=255,unique=True,blank=False,primary_key=True)
    title = models.CharField(max_length=255, blank=False, unique=False)
    description = models.CharField(max_length=255, blank=False, unique=False)
    published_date = models.DateField(blank=False, unique=False)
    seite50_sentence = models.CharField(max_length=4096, blank=False, unique=False)

    # Metadata
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.title)


class Author(models.Model):

    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255,unique=True,blank=False)
    publications = models.ManyToManyField(Book, related_name="authored_by", blank=True)

    # Metadata
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.name)