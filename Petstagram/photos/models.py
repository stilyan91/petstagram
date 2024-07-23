from django.core.validators import MinLengthValidator
from django.db import models

from Petstagram.pets.models import Pet
from .validators import validate_file_size


class Photo(models.Model):
    photo = models.ImageField(
        validators=[validate_file_size],
        upload_to='images')
    description = models.TextField(blank=True, null=True, max_length=300, validators=[MinLengthValidator(10)])
    location = models.CharField(max_length=30)
    tagged_pets = models.ManyToManyField(Pet, blank=True)
    date_of_publication = models.DateField(auto_now=True)

    def __str__(self):
        return f"{self.pk}--{self.photo}"
