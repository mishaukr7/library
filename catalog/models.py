from django.db import models
from datetime import date
from django.urls import reverse
# Create your models here.


class Author(models.Model):

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField('died', null=True, blank=True)
    biography = models.TextField(max_length=1000)
    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
    photo = models.ImageField(upload_to='media/author_photo', blank=True)

    class Meta:
        db_table = 'author'
        ordering = ['last_name', 'first_name']

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    def __str__(self):
        return '{0}, {1}'.format(self.last_name, self.first_name)


class Language(models.Model):
    name = models.CharField(max_length=200, help_text='Enter book natural language ex. English, Russian, Ukrainian etc.')

    class Meta:
        db_table = 'language'
        ordering = ['name']

    def __str__(self):
        return self.name


class Country(models.Model):
    name = models.CharField(max_length=200, help_text='Enter author natural country')

    class Meta:
        db_table = 'country'
        ordering = ['name']

    def __str__(self):
        return self.name


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    date_publication = models.DateField(null=True, blank=True)
    genre = models.ManyToManyField('Genre', help_text='Select genre to this book')
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)
    is_free = models.BooleanField()
    cover = models.ImageField(upload_to='media/book_cover', blank=True)

    def get_absolute_url(self):
        return reverse('author-detail', args=[str(self.id)])

    class Meta:
        db_table = 'book'
        ordering = ['-date_publication']

    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=100, help_text='Enter a book genre, e.g. Fantasy, Detective')

    class Meta:
        db_table = 'genre'
        ordering = ['name']

    def __str__(self):
        return self.name



