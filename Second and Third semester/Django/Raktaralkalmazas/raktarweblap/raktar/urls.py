from django.urls import path,include
from . import views

app_name="raktar"
urlpatterns = [
    path('',views.index,name="index"),
    path('addTermek',views.addTermek,name="addTermek"),
    path('deleteByUrl/<int:termekId>',views.deleteByUrl,name="deleteByUrl"),
    path('deleteByForm',views.deleteByForm,name="deleteByForm"),
    path('getdata',views.getData,name="getdata")
]