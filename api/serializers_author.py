from rest_framework import serializers
from .models_author import Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name', 'publications')
        read_only_fields = ('id', 'date_created', 'date_modified')