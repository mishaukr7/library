from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.login, {'template_name': 'login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page':'login'}, name='logout'),
    path('signup/', views.signup, name='signup'),
    path('profile/', views.ProfileView, name='view_profile'),
    path('profile/<int:pk>', views.ProfileViewWithPK, name='view_profile_with_pk'),
    path('profile/edit/', views.edit_profile, 'edit_profile'),
]