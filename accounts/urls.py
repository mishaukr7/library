from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.login, {'template_name': 'registration/login.html'}, name='login'),
    path('logout/', auth_views.logout, {'next_page':'login'}, name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    #path('profiles/', views.ProfileView, name='view_profile'),
    path('profile/<slug:slug>', views.ProfileDetailView.as_view(), name='user_profile'),
    #path('profile/edit/', views.edit_profile, 'edit_profile'),
    #path('user/settings/account'),
]