from django.urls import path

from . import views

# URL patterns for the 'hello' app

urlpatterns = [
    path("", views.index, name="index"),
    path("Issah", views.Issah, name="Issah"),
    path("<str:name>/", views.greet, name="greet"),
]
