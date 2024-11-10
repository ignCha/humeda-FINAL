from Applications.gallery import views
from django.urls import path



urlpatterns =[
    path('ListaPhotos/', views.GallerySection.as_view(), name='ListaPhotos'),
]

