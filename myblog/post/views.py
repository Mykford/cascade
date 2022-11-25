from django.shortcuts import render
from .models import Posts
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy
from .forms import CreateForm, EditForm

# Create your views here.

class HomePageView(ListView):
    queryset = Posts.objects.filter(status ='published')
    template_name = 'home.html'

class FullView(DetailView):
    model = Posts
    template_name = 'post_detail.html'    

class NewView(CreateView):
    model = Posts
    template_name = 'create.html'
    # fields = ['title','author','body','publish','status',]
    form_class = CreateForm

class EditView(UpdateView):
    model = Posts
    template_name = 'edit.html'
    # fields= ['title','body'] 
    form_class = EditForm  

class RemoveView(DeleteView):
    model = Posts
    template_name = 'delete.html'
    success_url = reverse_lazy('home')    