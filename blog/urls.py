from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("create", views.create, name="create"),
    path("preview", views.preview, name="preview"),
    path("blog/<slug:slug>", views.blog, name="blog"),
]
