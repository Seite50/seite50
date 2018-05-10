from django.shortcuts import render

from rest_framework import generics
from api.serializers.book import BookSerializer
from api.models.book import Book


class CreateBookView(generics.ListCreateAPIView):
    """
    Einfache view zum Anlegen von Büchern
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save()


class DetailsBookView(generics.RetrieveUpdateDestroyAPIView):
    """
    Einfache View zum Abrufen, Verändern, Löschen von Büchern
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
