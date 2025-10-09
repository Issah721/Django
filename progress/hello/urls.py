from django.urls import path

from . import views

# URL patterns for the 'hello' app

urlpatterns = [
    path("", views.index, name="index"),
]
