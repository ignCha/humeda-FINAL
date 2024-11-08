from django.db import models
from ckeditor.fields import RichTextField


class Content_Blocks(models.Model):
    Name = models.CharField(max_length=100)
    Option_section = (
        ('0', 'Home'),
        ('1', 'Galeria'),
        ('2', 'Noticias'),
        ('3', 'Recursos'),
        ('4', 'Reservas'),
    )
    Section = models.CharField('Seccion', max_length=2, choices=Option_section)
    Body = RichTextField(blank=True, null=True)


