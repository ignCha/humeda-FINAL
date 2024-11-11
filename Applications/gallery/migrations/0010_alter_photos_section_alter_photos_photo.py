# Generated by Django 5.1.3 on 2024-11-10 17:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0009_rename_section_section_photos_section'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photos',
            name='Section',
            field=models.CharField(blank=True, choices=[('0', 'general'), ('1', 'biodiversidad'), ('2', 'actividades'), ('3', 'amenazas')], max_length=2, verbose_name='Seccion'),
        ),
        migrations.AlterField(
            model_name='photos',
            name='photo',
            field=models.ImageField(upload_to='static/photos', verbose_name='img'),
        ),
    ]
