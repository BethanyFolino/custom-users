from django.shortcuts import render, HttpResponseRedirect, reverse
from customuser.models import MyUser
from customuser.forms import AddUserForm, LoginForm
from django.contrib.auth import login, authenticate, logout
from usertest.settings import AUTH_USER_MODEL
from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django import forms

# Create your views here.
def homepage(request):
    my_user = settings.AUTH_USER_MODEL
    # auth_user_model = AUTH_USER_MODEL
    return render(request, 'homepage.html', {'my_users': my_user})

def add_user(request):
    if request.method == "POST":
        form = AddUserForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            my_user1 = MyUser.objects.create_user(username=data['username'], password=data['password'], display_name=data['display_name'], homepage=data['homepage'], age=data['age'])
            login(request, my_user1)
            return HttpResponseRedirect(reverse('home'))
    form = AddUserForm()
    return render(request, 'generic_form.html', {'form': form})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            my_user = authenticate(request, username=data['username'], password=data['password'])
            if my_user:
                login(request, my_user)
                return HttpResponseRedirect(reverse('home'))

    form = LoginForm()
    return render(request, 'generic_form.html', {"form": form})

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.GET.get('next', reverse('home')))