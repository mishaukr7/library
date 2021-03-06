from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', auth_views.login, {'template_name': 'registration/login.html',
                                      'redirect_authenticated_user': 'True'}, name='login'),
    path('logout/', auth_views.logout, {'next_page': 'login'}, name='logout'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('profile/<slug:slug>', views.ProfileDetailView.as_view(), name='user_profile'),
]