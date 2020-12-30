from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.get_page, name="get_page"),
    path("randomPage/", views.get_random, name="get_random"),
    path("create/", views.create, name="create"),
    path("search/", views.search, name="search"),
    path("edit/<str:title>", views.edit, name="edit"),
]
