from django.shortcuts import render
from .models import Szak, Felvetelizo

# Create your views here.
def index(response):
   szakAllData = Szak.objects.all()
   felvetelizoAllData = Felvetelizo.objects.all()
   szakContext = {'all_szakData': szakAllData}
   felvContext = {'all_felvData': felvetelizoAllData}
   allContext = {**szakContext, **felvContext}
   return render(response, "index.html", allContext)