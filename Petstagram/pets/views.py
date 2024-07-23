from django.shortcuts import render, redirect

from Petstagram.pets.models import Pet
from .forms import PetAddForm, PetEditForm, PetDeleteForm


def pet_add(request):
    form = PetAddForm()

    if request.method == 'POST':
        form = PetAddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile-details', pk=1)
    context = {
        'form': form,
    }
    return render(request, 'pets/pet-add-page.html', context=context)


def pet_details(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).first()
    all_photos = pet.photo_set.all()
    context = {
        'pet': pet,
        'all_photos': all_photos,
    }
    return render(request, 'pets/pet-details-page.html', context=context)


def edit_pet(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).first()

    if request.method == 'GET':
        form = PetEditForm(instance=pet, initial=pet.__dict__)
    else:
        form = PetEditForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet_details', username, pet_name)
    context = {"form": form, 'pet_name': pet_name, 'username': username}
    return render(request, 'pets/pet-edit-page.html', context=context)


def delete_pet(request, username, pet_name):
    pet = Pet.objects.filter(slug=pet_name).first()
    form = PetDeleteForm(instance=pet)
    if request.method == 'POST':
        form = PetDeleteForm(request.POST, instance=pet)
        if form.is_valid():
            pet.delete()
            return redirect('profile-details', pk=1)
    context = {'form': form, 'pet_name': pet_name, 'username': username }

    return render(request, 'pets/pet-delete-page.html', context=context)

