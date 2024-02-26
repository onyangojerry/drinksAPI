from django.http import JsonResponse
from .models import Drink
from .serializers import DrinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

@api_view(['GET','POST'])
def drink_list(request, format=None):

    if request.method == 'GET':
        drinks = Drink.objects.all()
        sereializer = DrinkSerializer(drinks,  many=True)
        return Response(sereializer.data)

    if request.method == 'POST':
       serializer = DrinkSerializer(data=request.data)
       if sereializer.is_valid():
        sereializer.save()
        return Response(sereializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET','PUT','DELETE'])
def drink_detail(request, id, format=None):

    try:
        drink = Drink.objects.get(pk=id)
    except Drink.DoesNotExist:
        return Respoonse(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        sereializer = DrinkSerializer(drink)
        return Response(sereializer.data)
    elif request.method == 'PUT':
        serializer = DrinkSerializer(drink, data=request.data)
        if sereializer.is_valid():
            sereializer.save
            return Response(sereializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        drink.delete()
        return Response(status=status.http_204_NO_CONTENT)

