from django.shortcuts import render, get_object_or_404, redirect
from django.views import View, generic
from .models import *
from .forms import CommentForm
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods
from django.core.exceptions import ObjectDoesNotExist
from django.template.context_processors import csrf


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
    paginate_by = 12
    queryset = Book.objects.order_by('-date_add')


class BookDetailView(generic.DetailView):
    model = Book


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 10


class AuthorDetailView(generic.DetailView):
    model = Author


class GenreListView(generic.ListView):
    model = Genre
    paginate_by = 10


class GenreDetailView(generic.DetailView):
    model = Genre


@login_required
@require_http_methods(['POST'])
def add_comment(request, book):
    form = CommentForm(request.POST)
    book_id = get_object_or_404(Book, id=book)

    if form.is_valid():
        comment = Comment()
        comment.path = []
        comment.book = book_id
        comment.author = auth.get_user(request)
        comment.content = form.cleaned_data['comment_area']
        comment.save()

        try:
            comment.path.extend(Comment.objects.get(id=form.cleaned_data['parent_comment']).path)
            comment.path.append(comment.id)
        except ObjectDoesNotExist:
            comment.path.append(comment.id)

        comment.save()

    return redirect(book.get_absolute_url())

