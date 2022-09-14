from rest_framework import serializers
from .models import *

class GameSerializer(serializers.ModelSerializer):
    
    
    class Meta:
        model = Game
        exclude = ('active',)
     
    def to_representation(self, instance):
        

        return {
            'uuid': instance.uuid,
            'name': instance.name,
            'description': instance.description,
            'category':instance.category,
            'price': f'{instance.price}$',
            'size': f"{instance.size} {instance.um}'s",
            'plataform': instance.plataform.name if instance.plataform != None else '',
            'image': f'{instance.image.url}',
            
        }     
     

class PlataformSerializer(serializers.ModelSerializer):
    class Meta:
        model = Plataform
        exclude = ('active',)   

     
class MesureUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MesureUnit
        exclude = ('active',)   

     