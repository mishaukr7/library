from django import template
from catalog.models import *

register = template.Library()


@register.simple_tag
def get_book():
    books = Book.objects.all()[:5]
    return books


@register.simple_tag
def get_genre():
    genres = Genre.objects.all()[:5]
    return genres


@register.simple_tag
def get_author():
    authors = Author.objects.all()[:5]
    return authors



@register.simple_tag
def get_country():
    countries = Country.objects.all()[:5]
    return countries



