from django.shortcuts import render, get_object_or_404
from django.views import View
from catalog.models import *
# Create your views here.


class BasePageView(View):
    template_name = 'home/base.html'

    def get(self, request, *args, **kwargs):
        context = {}
        context['book_list'] = Book.objects.all().order_by('title')
        context['author_list'] = Author.objects.all()
        context['genre_list'] = Genre.objects.all()
        context['language_list'] = Language.objects.all()
        context['country_list'] = Country.objects.all().order_by('name')

        return render(request, template_name=self.template_name, context=context)