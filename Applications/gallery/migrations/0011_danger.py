# Generated by Django 5.1.3 on 2024-11-10 22:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0010_alter_photos_section_alter_photos_photo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Danger',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('image', models.ImageField(upload_to='static/dangerPhotos')),
            ],
        ),
    ]