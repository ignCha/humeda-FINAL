# Generated by Django 5.1.3 on 2024-11-10 03:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_photos_biodiversity'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos_biodiversity',
            name='photo',
            field=models.ImageField(upload_to='BioPhotos', verbose_name='img'),
        ),
    ]