from rest_framework import serializers
from .models import Book, Author


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['id', 'first_name', 'last_name', 'biography']


class BookSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=Author.objects.all())

    class Meta:
        model = Book
        fields = ['id', 'title', 'author', 'year_of_publication', 'genre', 'category', 'publisher', 'cover_image', 'file']

    def validate(self, data):
        title = data.get('title')
        author = data.get('author')

        if Book.objects.filter(title=title, author=author).exists():
            raise serializers.ValidationError("Книга с таким названием и автором уже существует")

        return data
