from ckeditor.fields import RichTextField
from django.db import models

# Create your models here.

class Photos(models.Model):
    name = models.CharField('nombre',max_length=30)
    photo = models.ImageField('img',upload_to='static/photos')
    description = models.TextField('descripcion', blank=True)
    Option_section = (
        ('0','general'),
        ('1', 'biodiversidad'),
        ('2', 'actividades'),
        ('3', 'amenazas'),
        ('4','flora')
    )
    Section= models.CharField('Seccion', max_length=2, choices=Option_section, blank=True)

    def __str__(self):
        return str(self.photo) + ' ' + str(self.Section)


class GallerySubSection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.id) + ' ' + self.name


class Danger(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to='static/dangerPhotos')


    def __str__(self):
        return self.title

class SectionFauna(models.Model):
    title = models.CharField('titulo',max_length=50)
    description = models.TextField('descripcion')
    photo = models.ImageField('img',upload_to='static/faunaPhotos')

    def __str__(self):
        return self.title
