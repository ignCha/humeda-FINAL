from Applications.gallery import views
from django.urls import path


from Applications.gallery.views import GalleryThreatSection


app_name = 'gallery-app'
urlpatterns =[
    path('ListaPhotos/', views.GallerySection.as_view(), name='ListaPhotos'),
    path('Amenazas/', views.GalleryThreatSection.as_view(), name='amenazas'),
    path('updateThreat/<pk>/',views.ThreatUpdate.as_view(), name='modifyThreat'),
    path('vistasFlora',views.vistasFloraFauna.as_view(), name='vistasFlora'),
]


