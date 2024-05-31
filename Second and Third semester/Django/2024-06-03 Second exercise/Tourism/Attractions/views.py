from django.shortcuts import redirect, render
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from rest_framework.decorators import api_view
from .models import TourismAttractions, Cities
from .serializers import TourismAttractionsSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def mainPage(request):
   if request.method == 'GET':
      return render(request, "home.html")

@api_view(['GET'])
def getAllAttractions(request):
   if request.method == 'GET':
      attractions = TourismAttractions.objects.all()
      serialized = TourismAttractionsSerializer(attractions, many=True)
      return JsonResponse(serialized.data, safe=False)
   
@api_view(['GET','POST'])
def addNewAttraction(request):
   if request.content_type == 'application/json':
      data = request.data
      inputCity = data['city']
      city = Cities.objects.get(name=inputCity)
      attraction_name = data['attraction_name']
      short_desc = data['short_desc']
      avg_rate = data['avg_rate']
      opening_hours = data['opening_hours']
      newAttraction = TourismAttractions(city=city, name=attraction_name, short_description=short_desc, average_rate=avg_rate, opening_hours=opening_hours)
      newAttraction.save()
      return Response(data, status=status.HTTP_201_CREATED)
   elif request.method == 'GET':
      return render(request, "post.html")
   else:
      return Response({'error':'Invalid content type'}, status=status.HTTP_400_BAD_REQUEST)
   
@api_view(['GET', 'DELETE'])
def deleteAttraction(request, id):
   if request.method == 'DELETE':
      TourismAttractions.objects.get(id=id).delete()
   return render(request, "home.html")