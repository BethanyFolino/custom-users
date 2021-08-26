from django.shortcuts import render, HttpResponseRedirect, reverse
from customuser.models import MyUser
from django.contrib.auth import login, authenticate, logout

# Create your views here.
def homepage(request):
    my_user = MyUser
    return render(request, 'homepage.html', {'my_users': my_user})

def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            user = authenticate(request, username=data['username'], password=data['password'])
            if user:
                login(request, user)
                return HttpResponseRedirect(request.GET.get('next', reverse('home')))
    form = LoginForm()
    return render(request, 'login_form.html', {"form": form})