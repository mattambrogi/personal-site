from django.urls import path
from .views import HomePageView, ProjectsView
from blog.views import NoteListView, BlogPostView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("projects", ProjectsView.as_view(), name="projects"),
    path("notes/", NoteListView.as_view(), name="notes"),
    path("notes/<slug:slug>/", BlogPostView.as_view(), name="note"),
]