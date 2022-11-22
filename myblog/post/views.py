from django.shortcuts import render
from .models import Posts
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.

class HomePageView(ListView):
    model = Posts
    template_name = 'home.html'

class FullView(DetailView):
    model = Posts
    template_name = 'post_detail.html'    

class NewView(CreateView):
    model = Posts
    template_name = 'create.html'
    fields = ['title','slug','author','body','publish','status',]

class EditView(UpdateView):
    model = Posts
    template_name = 'edit.html'
    fields= ['title','body']   

class RemoveView(DeleteView):
    model = Posts
    template_name = 'delete.html'
    success_url = reverse_lazy('home')    