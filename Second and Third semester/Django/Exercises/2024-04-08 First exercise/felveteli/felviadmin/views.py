from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Szak,Felvetelizo

def index(request):
   
   szakok=Szak.objects.all()
   felvetelizok=Felvetelizo.objects.all()
   context={"szakok":szakok, "felvetelizok":felvetelizok}

   if request.method == 'POST':
      nev = request.POST.get('name')
      szulEv = request.POST.get('year')
      pontszam = request.POST.get('score')
      szak = request.POST.get('szak')
      Felvetelizo.objects.create(nev=nev, szul_ev=szulEv, pontszam=pontszam, szak=Szak.objects.get(szakNev=szak))
   
   return render(request, "index.html", context)

def deleteFelvetelizo(request, id):
   Felvetelizo.objects.get(id=id).delete()
   return redirect(index)