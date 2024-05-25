from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from .models import Meres
from .serializers import MeresSerializer

# Create your views here.
@csrf_exempt
def returnJsonData(request):
   if request.method == 'GET':
      meresek = Meres.objects.all()
      serializer = MeresSerializer(meresek, many=True)
      return JsonResponse(serializer.data, safe=False)
   elif request.method == 'POST':
      data = JSONParser().parse(request)
      serializer = MeresSerializer(data=data)
      if serializer.is_valid():
         serializer.save()
         return JsonResponse(serializer.data, status=201)
      return JsonResponse(serializer.errors, status=400)