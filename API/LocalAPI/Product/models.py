from django.db import models

# Create your models here.
class Nomeclador(models.Model):
    uuid = models.BigAutoField(primary_key=True)
    name = models.CharField(verbose_name='Nombre',max_length = 150,unique=True)
    description = models.TextField(verbose_name='Descripción',blank=True) 
    
    def __str__(self) -> str:
        return self.name  
    class Meta:
        abstract = True

class Plataform(Nomeclador):
    class Meta:
        verbose_name = 'Plataforma'
        verbose_name_plural = 'Plataformas'

class MesureUnit(Nomeclador):
    class Meta:
        verbose_name = 'Unidad de Medida'
        verbose_name_plural = 'Unidades de Medidas'        

class BaseModel(models.Model):
    uuid = models.BigAutoField(primary_key=True)
    name = models.CharField(verbose_name='Nombre',max_length = 150,unique=True)
    description = models.TextField(verbose_name='Descripción',blank=True)
    price = models.FloatField(verbose_name='Precio')
    image = models.ImageField(verbose_name='Foto',upload_to='static', height_field=None, width_field=None, max_length=100)
    category = models.TextField(blank=True)
    mesure_unit = models.ForeignKey(MesureUnit, on_delete=models.SET(''),blank=True)
    active = models.BooleanField(verbose_name='Activo',default=True)

    def __str__(self) -> str:
        return self.name
    
    class Meta:
        abstract = True


class Game(BaseModel):
    
    plataform = models.ForeignKey(Plataform, on_delete=models.SET(''),blank=True)
    heigth = models.FloatField(verbose_name='Peso')
    

    class Meta:
        verbose_name = 'Juego'
        verbose_name_plural = 'Juegos'