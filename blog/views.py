from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post

# Create your views here.
class PostListView(ListView):
    model = Post
    template_name = "posts.html"
    ordering = ['-created_at']

class NoteListView(ListView):
    model = Post
    template_name = "notes.html"
    ordering = ['-created_at']
    context_object_name = 'note_list'

    def get_queryset(self):
        queryset = super().get_queryset().filter(note=True)
        return queryset


class BlogPostView(DetailView):
    model = Post
    template_name = "blog_post.html"