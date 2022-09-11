from rest_framework import serializers
from .models import *

class GameSerializer(serializers.ModelSerializer):
   
    class Meta:
        model = Game
        exclude = ('active',)   
     

class PlataformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataform
        exclude = ('active',)   

     
class MesureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesureUnit
        exclude = ('active',)   

     