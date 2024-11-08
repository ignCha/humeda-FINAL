
from django.urls import path
from Applications.Home import views

app_name = 'Home-app'
urlpatterns = [
    path('Home/', views.Home.as_view(), name='Home'),
    path('editar-home/<pk>/', views.EditContentHome.as_view(), name='EditContentHome'),
]
