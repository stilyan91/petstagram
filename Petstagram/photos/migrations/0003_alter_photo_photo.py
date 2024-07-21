# Generated by Django 5.0.7 on 2024-07-21 04:54

import Petstagram.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_date_of_publication_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='', validators=[Petstagram.photos.validators.validate_file_size]),
        ),
    ]
