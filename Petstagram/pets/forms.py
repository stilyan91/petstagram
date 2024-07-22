from django import forms
from .models import Pet


# FORM use when getting data not related to model ( note create model instance)
# MODEL FORM use when getting data related to model ( create model instance)

class PetAddForm(forms.ModelForm):
    class Meta:
        model = Pet
        field = '__all__'  # or [field1, ....]
        exclude = ['slug']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter Pet name', 'class': 'form-control'}),
            'date_of_birth': forms.DateInput(attrs={'placeholder': 'Enter date of birth', 'type': 'date'}),
            'personal_photo': forms.URLInput(attrs={'placeholder': 'Link to images', }),
        }
        labels = {
            'name': "Pet name",
            'personal_photo': "Pet photo",
            'date_of_birth': "Date of birth",
        }

class PetEditForm(forms.ModelForm):
    pass


class PetDeleteForm(forms.ModelForm):
    pass
