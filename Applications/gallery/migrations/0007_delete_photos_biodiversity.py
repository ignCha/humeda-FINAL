# Generated by Django 5.1.3 on 2024-11-10 03:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0006_alter_photos_biodiversity_photo'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Photos_bioDiversity',
        ),
    ]
