# Django shit
from django.http import HttpResponse
from django.views import View
from django.shortcuts import render
from rest_framework import viewsets

# Models and other stuff
from .models import Book
from .serializers import BookSerializer


# Here are a couple of examples of how to render raw HTML directly using Django.


# Through a class that makes HTML strings and are passed directly into a response.
class Another(View):
    books = Book.objects.all()
    if books:
        books_total = f"We have {len(books)} books in DB<br>"
        titles = "Titles in DB: <br>"
        for book in books:
            titles += f"{book.title}<br>"
        output = books_total + titles
    else:
        output = "No books in DB"

    def get(self, request):
        return HttpResponse(self.output)


# A function that uses a pre-defined HTML template (found in the templates folder), passes a data object to render
def first(request):
    books = Book.objects.all()
    return render(request, 'first_template.html', {"books": books})


# A ViewSet class for Django REST API to render entries/queryset into JSON objects.
class BookViewSet(viewsets.ModelViewSet):
    serializer_class = BookSerializer
    queryset = Book.objects.all()
