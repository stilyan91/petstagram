from django import forms

from .models import Photo

labels = {
    'pet_image': 'Photo file',
    'description': 'Description',
    'location': 'Location',
    'tagged_pets': 'Tag pets',
}


class BaseForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ['photo', 'description', 'location', 'tagged_pets']


class PhotoCreateForm(BaseForm):
    class Meta:
        model = Photo
        fields = ['photo', 'description', 'location', 'tagged_pets']
        labels = labels


class PhotoEditForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = ('photo', 'description', 'location', 'tagged_pets')
        exclude = ['pet_image']
        labels = labels


class PhotoDeleteForm(BaseForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
