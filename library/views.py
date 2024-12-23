from rest_framework.generics import ListCreateAPIView, RetrieveAPIView
from rest_framework.filters import SearchFilter
from .models import Book, Author
from .serializers import BookSerializer, AuthorSerializer
from rest_framework.permissions import IsAdminUser


class BookListCreateAPIView(ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'genre']

    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()


class AuthorListCreateAPIView(ListCreateAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name']

    permission_classes = [IsAdminUser]

    def perform_create(self, serializer):
        serializer.save()


class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class AuthorDetailView(RetrieveAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
