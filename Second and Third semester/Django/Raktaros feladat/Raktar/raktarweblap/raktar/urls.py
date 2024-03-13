from django.urls import path

from . import views
app_name="raktar"
urlpatterns = [
    path('',views.index,name="index")
]