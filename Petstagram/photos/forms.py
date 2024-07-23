from django import forms

from .models import Photo

class PhotoCreateForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'
        labels = {
            'pet_image': 'Photo file',
            'description': 'Description',
            'location': 'Location',
            'tagged_pets': 'Tag pets',
        }
