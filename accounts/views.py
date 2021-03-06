from .models import *
from django.views.generic.edit import CreateView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .forms import RegistrationForm
import json
from django.views import View
from django.contrib import auth
from django.http import HttpResponse
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


class BookmarkView(View):
    model = None

    def post(self, requset, pk):
        user = auth.get_user(requset)
        bookmark, created = self.model.objects.get_or_create(user=user, obj_id=pk)

        if not created:
            bookmark.delete()
        return HttpResponse(
            json.dumps({
                "result": created,
                "count": self.model.objects.filter(obj_id=pk).count()
            }),
            content_type='application/json'
        )













