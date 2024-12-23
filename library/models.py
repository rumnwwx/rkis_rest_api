from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    biography = models.TextField()

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name="books")
    year_of_publication = models.PositiveIntegerField(
        validators=[MinValueValidator(1000), MaxValueValidator(9999)],
        help_text="Год выпуска должен быть от 1000 до 9999"
    )
    genre = models.CharField(max_length=100)
    category = models.CharField(max_length=100)
    publisher = models.CharField(max_length=100)
    cover_image = models.ImageField(upload_to="covers/")
    file = models.FileField(upload_to="books/")

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["title", "author", "year_of_publication", "publisher"], name="unique_book")
        ]

    def __str__(self):
        return f"{self.title} by {self.author}"
