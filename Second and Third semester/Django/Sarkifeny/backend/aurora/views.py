from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from .models import Observation, City
from .serializers import ObservationSerializer, CitySerializer
from rest_framework.response import Response
from rest_framework import status

@api_view(['POST'])
def addNewObservation(request):
   if request.content_type == 'application/json':
      data = request.data
      _cityName = data['cityName']
      _city = City.objects.get(city=_cityName)
      _street = data['street']
      _observTime = data['observTime']
      _auroraType = data['auroraType']
      newElement = Observation(city=_city, street=_street, observTime=_observTime, auroraType=_auroraType)
      newElement.save()
      return Response(data, status=status.HTTP_201_CREATED)
   else:
      return Response({'error':'Invalid content type'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def getAllCity(request):
   if request.method == 'GET':
      cities = City.objects.all()
      serialized = CitySerializer(cities, many=True)
      return JsonResponse(serialized.data, safe=False)
   
@api_view(['DELETE'])
@csrf_exempt
def deleteObservation(request, id):
   if request.method == 'DELETE':
      searchedObservation = Observation.objects.get(pk=id)
      searchedObservation.delete()
      #return Response(searchedObservation, status=status.HTTP_200_OK)