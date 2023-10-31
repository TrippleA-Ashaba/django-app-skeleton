from django.urls import path

from .views import forms, home

urlpatterns = [
    path("", home, name="home"),
    path("forms/", forms, name="forms"),
]
