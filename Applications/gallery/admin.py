from django.contrib import admin

from Applications.gallery.models import Photos, GallerySubSection, Danger, SectionFauna

# Register your models here.

admin.site.register(Photos)
admin.site.register(GallerySubSection)
admin.site.register(Danger)
admin.site.register(SectionFauna)
