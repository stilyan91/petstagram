from django.shortcuts import render, redirect

from Petstagram.common.models import Like
from Petstagram.photos.models import Photo
from .forms import PhotoCreateForm, PhotoEditForm


def photo_add(request):
    form = PhotoCreateForm
    if request.method == 'POST':
        form = PhotoCreateForm(request.POST or None, request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect('index')
    context = {'form': form}
    return render(request, 'photo/photo-add-page.html', context=context)


def photo_details(request, pk):
   photo = Photo.objects.filter(pk=pk).first()
   like = photo.like_set.all()
   comments = photo.comment_set.all()

   context = {'photo': photo, 'like': like, 'comments': comments}

   return render(request, 'photo/photo-details-page.html', context=context)


def photo_edit(request, pk):
    photo = Photo.objects.filter(pk=pk).first()
    form = PhotoEditForm(request.POST, instance=photo)
    if form.is_valid():
        form.save()
        return redirect('photo_details', pk)
    context = {'form': form, "pk": pk }
    return render(request, 'photo/photo-edit-page.html',context=context)

def photo_delete(request, pk):
    photo = Photo.objects.filter(pk=pk).first()
    photo.delete()
    return redirect('index')
