from rest_framework import serializers
from api.models.author import Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ('id', 'name')
        read_only_fields = ('id', 'date_created', 'date_modified')
