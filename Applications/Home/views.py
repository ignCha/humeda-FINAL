from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import (ListView, DetailView, UpdateView)
from .models import *

# Create your views here.
class Home(ListView):
    model = Content_Blocks
    template_name = 'Home/home.html'
    context_object_name = 'content_blocks'

    def get_queryset(self):
        list_blocks = Content_Blocks.objects.filter(
            Section='0'
        )
        return list_blocks

class EditContentHome(UpdateView):
    model = Content_Blocks
    template_name = 'Home/editar_Home.html'
    context_object_name = 'content_blocks'
    fields = ['Body']
    success_url = reverse_lazy('Home-app:Home')

'''class Block_View(DetailView):
    model = Content_Blocks
    template_name = 'Home/Block_Detail.html'
    context_object_name = 'Block_Detail'''


