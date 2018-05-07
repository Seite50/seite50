from rest_framework import serializers
from .models import Book, Author


class BookSerializer(serializers.ModelSerializer):

    class Meta:
        model = Book
        fields = ('id', 'title', 'date_created', 'date_modified', 'description', 'published_date', 'seite50_sentence')
        read_only_fields = ('date_created', 'date_modified')


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'publications')
        read_only_fields = ('id', 'date_created', 'date_modified')