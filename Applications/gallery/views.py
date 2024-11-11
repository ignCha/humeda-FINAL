from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ( ListView,
                                   UpdateView )

    
from .models import Photos, Danger, SectionFauna



# Create your views here.

class GallerySection(ListView):
    model = Photos
    template_name = 'gallery/galleryPhotos.html'
    context_object_name = 'photos_gallery'

class GalleryThreatSection(ListView):
    model = Photos
    template_name = 'gallery/amenazas.html'
    context_object_name = 'photos_gallery'

class ThreatUpdate(UpdateView):
    model = Danger
    template_name = 'gallery/amenazasUpdate.html'
    context_object_name = 'infoUpdateAmenaza'
    fields = ['title', 'description']

class vistasFloraFauna(ListView):
    model = SectionFauna
    template_name = 'gallery/galleryPhotos.html'
    context_object_name = 'floraView'


