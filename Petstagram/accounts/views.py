from django.contrib.auth.decorators import login_required
from django.shortcuts import render


def register(request):
    return render(request, 'accounts/register-page.html', )


def login_user(request):
    return render(request, 'accounts/login-page.html', )


def logout_user(request):
    pass


def show_profile(request, pk):
    return render(request, 'accounts/profile-details-page.html', )


def edit_profile(request, pk):
    return render(request, 'accounts/profile-edit-page.html', )


def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html', )