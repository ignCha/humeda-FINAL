from django.db import models

# Create your models here.

class Photos(models.Model):
    name = models.CharField('nombre',max_length=30)
    photo = models.ImageField('img',upload_to='photos')
    description = models.TextField('descripcion', blank=True)
    def __str__(self):
        return str(self.photo)


class GallerySubSection(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return str(self.id) + ' ' + self.name


