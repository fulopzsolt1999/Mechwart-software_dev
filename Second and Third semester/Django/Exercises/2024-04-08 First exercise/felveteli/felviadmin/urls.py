from django.urls import path
from . import views

urlpatterns = [
    path("felviadmin/", views.index, name="index"),
    path("handle_register/", views.handle_register, name="handle_register")
]
