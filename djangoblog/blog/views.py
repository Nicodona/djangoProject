from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import POst
from django.urls import reverse_lazy

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

class BlogUpdateView(UpdateView):
    model = POst
    fields = ['tittle', 'body']
    template_name = 'edit.html'

class BlogDeleteView(DeleteView):
    model = POst
    template_name = 'delete.html'
    success_url = reverse_lazy('home')

