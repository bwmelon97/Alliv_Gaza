from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth

def signup(request):
    if request.method == 'POST':
        if request.POST['password'] == request.POST['password-confirm']:
            user = User.objects.create_user(
                username=request.POST['username'],
                password=request.POST['password']
            )
            auth.login(request, user)
            return render(request, 'accounts/signup.html')
        return render(request, 'accounts/signup.html')

    return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        input_id = request.POST['username']
        input_pw = request.POST['password']
        user = auth.authenticate(request, username=input_id, password=input_pw)
        if user is not None:
            auth.login(request, user)
            return redirect('accounts:test')
        return render(request, 'accounts/login.html', {'error': "username or password is not correct."})

    return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('accounts:test')
    return redirect('accounts:test')


def test(request):
    pass