# blog/views.py

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView
# from .forms import PostForm
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-id')  # Ordering should be applied here
    return render(request, 'blog/post_list.html', {'posts': posts})

# Create new post
class CreatePostView(CreateView):
    model = Post
    template_name = 'blog/create_post.html'
    # form_class = PostForm
    # fields = '__all__'
    fields = ['title', 'author', 'author_name', 'content', 'updated_on', 'image', 'video']
    # success_url = reverse_lazy('post_list')


class DetailView(DetailView):
    model = Post
    template_name = 'blog/detail_post.html'

class EditPostView(UpdateView):
    model = Post
    template_name = 'blog/edit.html'
    # fields = '__all__'
    fields =['title','author_name','content', 'updated_on', 'image', 'video']

class DeletePostView(DeleteView):
    model = Post
    template_name = 'blog/delete.html'
    success_url = reverse_lazy('post_list')



