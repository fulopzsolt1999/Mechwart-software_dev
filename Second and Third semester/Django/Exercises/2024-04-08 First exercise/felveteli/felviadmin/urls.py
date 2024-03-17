from django.urls import path
from . import views

urlpatterns = [
    path("felviadmin/", views.index, name="index")
]
