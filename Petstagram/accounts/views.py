from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from Petstagram.pets.models import Pet


def register(request):
    return render(request, 'accounts/register-page.html', )


def login_user(request):
    return render(request, 'accounts/login-page.html', )


def logout_user(request):
    pass


def profile_details(request, pk):
    pets = Pet.objects.all()
    context = {'pets': pets}

    return render(request, 'accounts/profile-details-page.html', context=context)


def edit_profile(request, pk):
    return render(request, 'accounts/profile-edit-page.html', )


def delete_profile(request, pk):
    return render(request, 'accounts/profile-delete-page.html', )
