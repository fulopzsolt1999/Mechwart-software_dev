from django.shortcuts import render, redirect
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import TourismAttractions, Countries, Cities
from .serializers import TourismAttractionsSerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET'])
def mainPage(request):
   if request.method == 'GET':
      return render(request, "mainPage.html")

@api_view(['GET'])
def getAllAttractions(request):
   if request.method == 'GET':
      attractions = TourismAttractions.objects.all()
      serialized = TourismAttractionsSerializer(attractions, many=True)
      return JsonResponse(serialized.data, safe=False)
   
@api_view(['POST'])
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
   else:
      return Response({'error':'Invalid content type'}, status=status.HTTP_400_BAD_REQUEST)