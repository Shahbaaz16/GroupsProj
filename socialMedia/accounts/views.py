from django.shortcuts import render
from django.views.generic import CreateView
from accounts import forms
from django.urls import reverse_lazy


class SignUp(CreateView):
    form_class = forms.UserCreateForm
    success_url = reverse_lazy('login')
    template_name = 'accounts/signup.html'
