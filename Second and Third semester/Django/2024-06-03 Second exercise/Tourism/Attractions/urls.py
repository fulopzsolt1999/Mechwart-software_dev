from django.urls import path
from . import views

urlpatterns = [
    path('getAllAttractions', views.getAllAttractions),
    path('newAttraction', views.addNewAttraction),
    path('deleteAttraction/<int:id>', views.deleteAttraction),
    path('', views.mainPage, name="mainPage")
]