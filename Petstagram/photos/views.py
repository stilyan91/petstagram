from django.shortcuts import render

from Petstagram.common.models import Like
from Petstagram.photos.models import Photo


def photo_add(request):
    return render(request, 'photo/photo-add-page.html')


def photo_details(request, pk):
   photo = Photo.objects.filter(pk=pk).first()
   like = photo.like_set.all()
   comments = photo.comment_set.all()

   context = {'photo': photo, 'like': like, 'comments': comments}

   return render(request, 'photo/photo-details-page.html', context=context)


def photo_edit(request, pk):
    return render(request, 'photo/photo-edit-page.html')
