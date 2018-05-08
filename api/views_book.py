from django.shortcuts import render

from rest_framework import generics
from .serializers_book import BookSerializer
from .models_book import Book

class CreateBookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsBookView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer