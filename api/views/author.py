from django.shortcuts import render

from rest_framework import generics
from api.serializers.author import AuthorSerializer

from api.models.author import Author


class CreateAuthorView(generics.ListCreateAPIView):
    """
    Einfache view zum Anlegen von Authoren
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailsAuthorView(generics.RetrieveUpdateDestroyAPIView):
    """
    Einfache View zum Abrufen, Verändern, Löschen von Authoren
    """
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer