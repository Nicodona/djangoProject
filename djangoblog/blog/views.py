from django.shortcuts import render
from django.views.generic import ListView
from .models import POst

class BlogListView(ListView):
    model = POst
    template_name = 'home.html'

