from django.shortcuts import render
from rest_framework import viewsets  # <- import viewsets
from .models import Book, Author  # <- don't forget your models
from .serializers import BookSerializer, AuthorSerializer  # <- or serializers


class BookViewSet(viewsets.ModelViewSet):
    # add code here
    serializer_class = BookSerializer
    queryset = Book.objects.all()

class AuthorViewSet(viewsets.ModelViewSet):
    # add code here
    serializer_class = AuthorSerializer
    queryset = Author.objects.all()
