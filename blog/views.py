from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "posts.html"
    ordering = ['-created_at']

class BlogPostView(DetailView):
    model = Post
    template_name = "blog_post.html"
    