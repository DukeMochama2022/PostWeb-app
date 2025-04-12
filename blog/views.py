from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin,UserPassesTestMixin
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
from .models import Post
from django.urls import reverse_lazy

# def home(request):
#     posts=Post.objects.all().order_by('-date_posted')
    
#     context={
#         'posts':posts
#     }
#     return render(request, "blog/index.html",context)
class PostListView(ListView):
    model=Post
    template_name='blog/index.html'
    context_object_name='posts'
    ordering=['-date_posted']

class PostDetailView(DetailView):
    model=Post

class PostCreateView(LoginRequiredMixin ,CreateView):
    model=Post    
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin, UpdateView):
    model=Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.author=self.request.user
        messages.success(self.request, "Post updated successfully!") 
        return super().form_valid(form)

    def test_func(self) :
        post=self.get_object()
        if self.request.user ==post.author:
            return True
        return False   

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model=Post
    success_url= reverse_lazy('blog:posts')

    def test_func(self) :
        post=self.get_object()
        if self.request.user ==post.author:
            messages.success(self.request, "Post deleted successfully!") 
            return True
        return False 

def about(request):
    return render(request,'blog/about.html')