from django.shortcuts import render
from django.views.generic import ListView
from .models import Photos

# Create your views here.

class GallerySection(ListView):
    model = Photos
    template_name = 'gallery/galleryPhotos.html'
    context_object_name = 'photos_gallery'

    # <div class="gallery"  >
    #        <img class="img-fluid img-gallery" src="{% static 'photos/images_1.jpeg' %}" alt="humedal">
    #         <img class="img-fluid img-gallery "  src="{% static 'photos/images.jpeg' %}" alt="humedal">
    #          <img class="img-fluid img-gallery "  src="{% static 'photos/humedales-1-e1611254064479-1024x524.jpg' %}" alt="humedal">
    #         <img class="img-fluid img-gallery "  src="{% static 'photos/images_1.jpeg' %}" alt="humedal">
    #     </div>