from django.shortcuts import render

from rest_framework import generics
from .serializers import BookSerializer, AuthorSerializer
from .models import Book, Author

class CreateBookView(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsBookView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Book.objects.all()
    serializer_class = BookSerializer


class CreateAuthorView(generics.ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

    def perform_create(self, serializer):
        serializer.save()

class DetailsAuthorView(generics.RetrieveUpdateDestroyAPIView):

    queryset = Author.objects.all()
    serializer_class = AuthorSerializer