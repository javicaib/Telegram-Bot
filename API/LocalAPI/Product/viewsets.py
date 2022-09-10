from email.mime import image
from rest_framework.response import Response
from rest_framework import status,viewsets
from .models import *
from .serializer import *

class GameViewset(viewsets.ModelViewSet):
    serializer_class = GameSerializer
    queryset = Game.objects.filter(active=True)

 

class PlataformViewset(viewsets.ModelViewSet):
    serializer_class = PlataformSerializer
    queryset = Plataform.objects.filter(active=True)
    


class MesureUnitViewset(viewsets.ModelViewSet):
    serializer_class = MesureUnitSerializer
    queryset = MesureUnit.objects.filter(active=True)
    



