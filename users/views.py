from django.shortcuts import render


def login(request):
    context = {
        'title': 'Log In',
    }
    return render(request, 'users/login.html', context)

def registration(request):
    context = {
        'title': 'Registration',
    }
    return render(request, 'users/registration.html', context)


def profile(request):
    context = {
        'title': 'My Profile',
    }
    return render(request, 'users/profile.html', context)


def logout(request):
    ...
