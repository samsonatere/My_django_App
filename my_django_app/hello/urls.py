from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("<str:name>", views.greet, name="greet"),
    path("samson", views.samson, name="samson"),
    path("atere", views.atere, name="atere")
]