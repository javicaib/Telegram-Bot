from rest_framework import routers
from .viewsets import *
from django.urls import path

router = routers.DefaultRouter()
router.register('game',GameViewset,basename='Game')
router.register('plataform',PlataformViewset,basename='Plataform')
router.register('mesure-unit',MesureUnitViewset,basename='MesureUnit')

urlpatterns = router.urls