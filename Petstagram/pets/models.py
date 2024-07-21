from django.db import models
from django.utils.text import slugify


class Pet(models.Model):
    name = models.CharField(max_length=50)
    personal_photo = models.URLField(max_length=500)
    date_of_birth = models.DateField(blank=True, null=True)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}--{self.pk}")
        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.slug}"