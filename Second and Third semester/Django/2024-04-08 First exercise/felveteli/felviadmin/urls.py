from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("deleteFelvetelizo/<int:id>", views.deleteFelvetelizo, name="deleteFelvetelizo")
]