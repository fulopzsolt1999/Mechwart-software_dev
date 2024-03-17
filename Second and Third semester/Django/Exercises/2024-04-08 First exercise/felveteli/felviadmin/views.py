from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Szak, Felvetelizo

# Create your views here.
def index(request):
   szakContext = {'all_szakData': Szak.objects.all()}
   felvContext = {'all_felvData': Felvetelizo.objects.all()}
   allContext = {**szakContext, **felvContext}
   return render(request, "index.html", allContext)

def handle_register(request):
   if request.method == 'POST':
      name = request.POST.get('name')
      szul_ev = request.POST.get('szul_ev')
      pontszam = request.POST.get('pontszam')
      szak = request.POST.get('szak')
      Felvetelizo.objects.create(szak=szak, name=name, szul_ev=szul_ev, pontszam=pontszam)
      return HttpResponse("Data successfully inserted!")
   else:
      return HttpResponse("Invalid request method.")