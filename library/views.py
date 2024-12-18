from rest_framework import generics
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer


class BookListView(generics.ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def get_queryset(self):
        queryset = Book.objects.all()
        title = self.request.query_params.get('title', None)
        genre = self.request.query_params.get('genre', None)
        author_name = self.request.query_params.get('author', None)

        if title:
            queryset = queryset.filter(title__icontains=title)
        if genre:
            queryset = queryset.filter(genre__icontains=genre)
        if author_name:
            queryset = queryset.filter(author__first_name__icontains=author_name) | queryset.filter(author__last_name__icontains=author_name)

        return queryset


class BookDetailView(generics.RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorListView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer


class AuthorDetailView(generics.RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
