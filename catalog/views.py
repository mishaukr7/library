from django.shortcuts import render, get_object_or_404
from django.views import View, generic
# Create your views here.

from .models import *


class SideBarView(View):
    template_name = 'catalog/index.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['book_list'] = Book.objects.all().order_by('date_add')[:10]
        context['author_list'] = Author.objects.all()
        context['genre_list'] = Genre.objects.all()
        context['language_list'] = Language.objects.all()
        context['country_list'] = Country.objects.all().order_by('name')

        return render(request, template_name=self.template_name, context=context)


class BookListView(generic.ListView):
    model = Book
    paginate_by = 10


class BookDetailView(generic.DetailView):
    mode = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(View):
    model = Author

