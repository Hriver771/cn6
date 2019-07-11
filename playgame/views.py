from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from playgame.models import Stones
from playgame.serializers import StoneSerializer
from rest_framework import generics
from django.http import JsonResponse
from django.core.serializers import serialize

from .models import Stones

def index(request):
    stoneList = Stones.objects.all()
    data = {'stoneList': stoneList}
    return render(request, 'playgame/index.html', data)

class userAPI(generics.ListCreateAPIView):
    queryset = Stones.objects.all()
    serializer_class = StoneSerializer

class getStones(generics.ListCreateAPIView):
    queryset = Stones.objects.all()
    serializer_class = StoneSerializer 

