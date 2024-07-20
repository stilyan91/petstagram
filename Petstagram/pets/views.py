from django.shortcuts import render


def pet_add(request):
    return render(request, 'pets/pet-add-page.html')


def pet_details(request, username, pet_name):
    return render(request, 'pets/pet-details-page.html')


def edit_pet(request, username, pet_name):
    return render(request, 'pets/pet-edit-page.html')


def delete_pet(request, username, pet_name):
    return render(request, 'pets/pet-delete-page.html')
