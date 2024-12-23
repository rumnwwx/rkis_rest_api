from django.urls import path
from .views import BookListCreateAPIView, BookDetailView, AuthorListCreateAPIView, AuthorDetailView

urlpatterns = [
    path('books/', BookListCreateAPIView.as_view(), name='book-list'),
    path('books/<int:pk>/', BookDetailView.as_view(), name='book-detail'),
    path('authors/', AuthorListCreateAPIView.as_view(), name='author-list'),
    path('authors/<int:pk>/', AuthorDetailView.as_view(), name='author-detail'),
]