from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def do_login(request):
    return render(request, 'registration/login.html', {})


def do_auth(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('../game')
    else:
        return redirect('login')