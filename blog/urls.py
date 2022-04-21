from django.urls import path
from .views import PostListView, BlogPostView

urlpatterns = [
    path("", PostListView.as_view(), name="posts"),
    path("<slug:slug>/", BlogPostView.as_view(), name="blog_post"),
]