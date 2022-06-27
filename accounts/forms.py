from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=200)
    email = forms.EmailField()
    password1 = forms.PasswordInput()
    password2 = forms.PasswordInput()



    # class Meta:
    #     model = User
    #     fields = ['username', 'email', 'password1', 'password2']