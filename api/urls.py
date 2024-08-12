from django.urls import path
from . import views

urlpatterns = [
    path("", views.pepe, name="index"),
]
