from django.shortcuts import render ,get_object_or_404
from .models import Posts, Categories
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from django.urls import reverse_lazy,reverse
from .forms import CreateForm, EditForm
from django.http import HttpResponseRedirect

# Create your views here.

def like(request,pk):
    post = get_object_or_404(Posts, id=request.POST.get('post_id'))
    post.likes.add(request.user)
    return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))

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


 # Creating Category View
class CategoryView(CreateView):
    model = Categories
    template_name = 'add_category.html'
    fields = '__all__'

# def FullCategoryView(request, cats):
#     category_posts =Posts.objects.filter(category=cats),
#     return render(request,'categories.html',{'category_posts':category_posts, 'cats':cats })

# class AllCategoryView(ListView):
#     def get_queryset(self):
#         return Categories.objects.filter(id=self.kwargs['id'])
    

          