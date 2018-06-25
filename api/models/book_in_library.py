from django.db import models
from api.models.user import User


# Create your models here.
class Library(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255, blank=False, unique=True)

    owner = models.ManyToManyField(User, related_name="organized_by", blank=False)

    # Metadata
    date_created = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)
