from django.urls import path, include

from . import views


app_name = 'catalog'

urlpatterns = [
    path('', views.SideBarView.as_view(), name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('authors/', views.AuthorListView.as_view(), name='authors'),
    path('authors/<int:pk>', views.AuthorDetailView.as_view(), name='author-detail'),
    path('genres/', views.GenreListView.as_view(), name='genres'),
    path('genres/<int:pk>', views.GenreDetailView.as_view(), name='genre-detail'),
    path('comment/<int:book>', views.add_comment, name='add_comment'),

]



