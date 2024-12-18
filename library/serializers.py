from rest_framework import serializers
from .models import Book, Author, Textbook

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'biography']

class BookSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'year_of_publication', 'genre', 'category', 'publisher', 'cover_image', 'file']

class TextbookSerializer(BookSerializer):
    edition = serializers.IntegerField()

    class Meta:
        model = Textbook
        fields = ['id', 'title', 'author', 'year_of_publication', 'genre', 'category', 'publisher', 'cover_image', 'file', 'edition']
