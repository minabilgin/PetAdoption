from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages

# Create your views here.


def homePage(request):
    return render(request, 'homePage.html', {})


def login_request(request):
    print("login req")
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(request, username=username, password=password)
    userid = user
    if user is not None:
        login(request, user)
        print("login not null")
        return redirect('/', {'logged_in'})
    else:
        messages.error(request, 'username or password not correct')
        print("login null")
        return redirect('/')


def logout_request(request):
    if request.method == "POST":
        logout(request)
    return redirect('homePage')

