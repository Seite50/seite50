from django.shortcuts import render

from rest_framework import generics
from api.serializers.book import BookSerializer
from api.models.book import Book

class CreateBookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsBookView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer