from django.shortcuts import render

from api.models.book import Book


def index(request):
    book_list = Book.objects.get()
    context = {
        'book_list': [book_list],
    }
    return render(request, 'book/index.html', context)