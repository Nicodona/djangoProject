from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from .models import POst

class BlogListView(ListView):
    model = POst
    template_name = 'home.html'

class BlogDetailView(DetailView):
    model = POst
    template_name = 'detail.html'

class BlogCeateView(CreateView):
    model = POst
    fields = ['tittle', 'author', 'body']
    template_name = 'new.html'