from django import forms
from django.contrib.auth.models import AbstractUser
from customuser.models import MyUser

class AddUserForm(forms.Form):
    homepage = forms.URLField()
    display_name = forms.CharField(max_length=30)
    age = forms.IntegerField()
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)