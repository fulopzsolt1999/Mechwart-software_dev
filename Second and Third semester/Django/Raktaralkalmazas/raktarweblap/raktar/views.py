from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import Termek,Kategoria
from .serializers import TermekSerializer

# Create your views here.

def index(request):
    termekLista=Termek.objects.all()
    kategoriaLista=Kategoria.objects.all().order_by("kategoriaNev")
    context={"termekLista":termekLista,"kategoriaLista":kategoriaLista}
    return render(request,"raktar/index.html",context)

def addTermek(request):
    _termeknev=request.POST["termeknev"]
    _ar=request.POST["ar"]
    _db=request.POST["db"]
    knev=request.POST["kategoria"]
    _termekkategoria=Kategoria.objects.get(kategoriaNev=knev)
    ujTermek=Termek(termekNev=_termeknev,ar=_ar,db=_db,kategoria=_termekkategoria)
    ujTermek.save()
    return redirect("/raktar")

def deleteByUrl(request,termekId):
    torlendo=Termek.objects.get(pk=termekId)
    torlendo.delete()
    return redirect("/raktar")

def deleteByForm(request):
    torlendoId=request.POST["termekId"]
    torlendo=Termek.objects.get(pk=torlendoId)
    torlendo.delete()
    return redirect("/raktar")

def getData(request):
    if (request.method == "GET"):
        termekek=Termek.objects.all()
        serialized=TermekSerializer(termekek,many=True)
        return JsonResponse(serialized.data,safe=False)