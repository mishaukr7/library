from .models import User
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

# Create your views here.


class SignUpView(CreateView):
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('login')
    model = User
    fields = ('username', 'password', 'first_name', 'last_name', 'email')
    #fields = ('bio', 'date_birth')


class ProfileDetailView(DetailView):
    model = User
    template_name = 'registration/profile.html'
    slug_field = 'username'
    context_object_name = 'user_profile'
