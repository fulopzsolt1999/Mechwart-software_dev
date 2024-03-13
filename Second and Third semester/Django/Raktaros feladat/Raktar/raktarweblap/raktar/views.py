from django.shortcuts import render
from django.http import HttpResponse

from .models import Termek,Kategoria

# Create your views here.

def index(request):
    termeklista=Termek.objects.all()
    context={"termeklista":termeklista}
    return render(request,"raktar/index.html",context)