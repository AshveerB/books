from django.db import models

# Create your models here.


class Author(models.Model):
    name = models.CharField(max_length=200)
    nationality = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        Author, on_delete=models.CASCADE, related_name='books')
    publication_year = models.PositiveIntegerField()
    book_cover = models.ImageField(
        upload_to='covers/%Y/%m/%d', max_length=300, null=True, blank=True)
    def __str__(self):
        return self.title
