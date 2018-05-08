from django.shortcuts import render

from rest_framework import generics
from .serializers_author import AuthorSerializer

from .models_author import Author

class CreateAuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsAuthorView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer