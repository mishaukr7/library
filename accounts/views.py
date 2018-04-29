from .models import *
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .forms import RegistrationForm

# Create your views here.


class SignUpView(CreateView):
    model = User
    form_class = RegistrationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')


class ProfileDetailView(DetailView):
    model = User
    template_name = 'registration/profile.html'
    slug_field = 'username'
    context_object_name = 'user_profile'















