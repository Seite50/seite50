from rest_framework import serializers
from api.models.book import Book


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('id', 'bookid', 'title', 'date_created', 'date_modified',
                  'description', 'published_date', 'seite50_sentence')
        read_only_fields = ('date_created', 'date_modified')
