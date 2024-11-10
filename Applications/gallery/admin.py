from django.contrib import admin

from Applications.gallery.models import Photos, GallerySubSection

# Register your models here.

admin.site.register(Photos)

admin.site.register(GallerySubSection)