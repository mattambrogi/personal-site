from django.urls import path
from .views import PostListView, BlogPostView
from .feeds import MostRecentPostsFeed

urlpatterns = [
    path("", PostListView.as_view(), name="posts"),
    path("feed/", MostRecentPostsFeed()),
    path("<slug:slug>/", BlogPostView.as_view(), name="blog_post"),
]