from django.urls import path
from .views import HomePageView, ProjectsView

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("projects", ProjectsView.as_view(), name="projects"),
]