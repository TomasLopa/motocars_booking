from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, get_user_model
from django.views import generic
from django.urls import reverse_lazy
# Create your views here.


class SignUpForm(UserCreationForm):
    class Meta:
        model = get_user_model()
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')


class SignUpView(generic.CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('home')
    template_name = 'signup.html'