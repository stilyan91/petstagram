from django.shortcuts import render


def photo_add(request):
    return render(request, 'photo/photo-add-page.html')


def photo_details(request, pk):
    return render(request, 'photo/photo-details-page.html')


def photo_edit(request, pk):
    return render(request, 'photo/photo-edit-page.html')
