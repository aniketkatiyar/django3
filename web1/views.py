from django.shortcuts import render, HttpResponseRedirect
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout


# Create your views here.


def index(request):
    return render(request, "index.html")
# Create your views here.

# Sinup View


def sign_up(request):
    if request.method == "POST":
        fm = SignUpForm(request.POST)
        if fm.is_valid():
            messages.success(request, 'Account Created Successfully !!')
            fm.save()
    else:
        fm = SignUpForm()
    return render(request, 'signup.html', {'form': fm})


def about(request):
    return render(request, "about.html")


def services1(request):
    return render(request, "services1.html")


def services2(request):
    return render(request, "services2.html")


def contact(request):
    return render(request, "contact.html")


def blog(request):
    return render(request, "blog.html")


# Login View Function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            fm = AuthenticationForm(request=request, data=request.POST)
            if fm.is_valid():
                uname = fm.cleaned_data['username']
                upass = fm.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully !!')
                    return HttpResponseRedirect('/profile/')
        else:
            fm = AuthenticationForm()
        return render(request, 'login.html', {'form': fm})
    else:
        return HttpResponseRedirect('/profile/')

# Profile


def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')

# Logout


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')
