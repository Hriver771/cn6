from django.shortcuts import render

# Create your views here.

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from playgame.models import Stones
from playgame.serializers import StoneSerializer
from rest_framework import generics

from .models import Stones

def index(request):
    stoneList = Stones.objects.all()
    context = {'stoneList': stoneList}
    return render(request, 'playgame/index.html', context)

class userAPI(generics.ListCreateAPIView):
    queryset = Stones.objects.all()
    serializer_class = StoneSerializer

