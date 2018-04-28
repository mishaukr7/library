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
    paginate_by = 18
    queryset = Book.objects.order_by('-date_add')


class BookDetailView(View):
    template_name = 'catalog/book_detail.html'
    comment_form = CommentForm

    def get(self, request, *args, **kwargs):
        book = get_object_or_404(Book, id=self.kwargs['book_id'])
        context = {}
        context.update(csrf(request))
        user = auth.get_user(request)
        context['book'] = book
        context['comments'] = book.comment_set.all().order_by('path')
        context['next'] = book.get_absolute_url()
        if user.is_authenticated:
            context['form'] = self.comment_form
        return render(request, template_name=self.template_name, context=context)


@login_required
@require_http_methods(['POST'])
def add_comment(request, book_id):
    form = CommentForm(request.POST)
    book = get_object_or_404(Book, id=book_id)

    if form.is_valid():
        comment = Comment()
        comment.path = []
        comment.book_id = book
        comment.author_id = auth.get_user(request)
        comment.content = form.cleaned_data['comment_area']
        comment.save()

        try:
            comment.path.extend(Comment.objects.get(id=form.cleaned_data['parent_comment']).path)
            comment.path.append(comment.id)
        except ObjectDoesNotExist:
            comment.path.append(comment.id)

        comment.save()

    return redirect(book.get_absolute_url())


class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 30
    queryset = Author.objects.order_by('-last_name')


class AuthorDetailView(generic.DetailView):
    model = Author


class GenreListView(generic.ListView):
    model = Genre
    paginate_by = 30


class GenreDetailView(generic.DetailView):
    model = Genre








