from django.urls import path
from . import views

urlpatterns = [
    path('getAllAttractions', views.getAllAttractions),
    path('newAttraction', views.addNewAttraction),
    path('', views.mainPage, name="mainPage")
]