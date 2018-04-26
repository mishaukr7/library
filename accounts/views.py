from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.template import RequestContext
from library.accounts.forms import SignUpForm
from django.contrib.auth import login, authenticate
from .models import User
from django.views import generic
from django.urls import reverse
# Create your views here.


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()
            user.profile.location = form.cleaned_data.get('location')
            user.save()
            raw_password = form.clean_password1('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect(reverse('books'))
        else:
            form = SignUpForm()
        return render(request, 'registration/signup.html', {'form': form})


class ProfileView(generic.DetailView):
    model = User
    template_name = 'registration/profile.html'
