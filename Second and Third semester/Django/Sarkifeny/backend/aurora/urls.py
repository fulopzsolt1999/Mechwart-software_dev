from django.urls import path
from . import views

urlpatterns = [
    path('newObservation', views.addNewObservation, name="newObservation"),
    path('getAllCities', views.getAllCity, name="getAllCities"),
    path('deleteObservation/<int:id>', views.deleteObservation, name="deleteObservation")
]