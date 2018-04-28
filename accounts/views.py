from .models import User, Profile
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

# Create your views here.


class SignUpView(CreateView):
    model = User
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    fields = ['username', 'email', 'password', 'first_name', 'last_name']


class ProfileDetailView(DetailView):
    model = User
    template_name = 'registration/profile.html'
    slug_field = 'username'
    context_object_name = 'user_profile'
