from ast import Return
from django.db import models
from django.db.models.deletion import RESTRICT
from django.db.models.fields import CharField, DateField, DateTimeField, FloatField, IntegerField, TextField

import equipment

# Create your models here.

class Equipment(models.Model):
    nombre = models.CharField(max_length = 50, null = False, blank = False, verbose_name = 'Nombre')
    imagen = models.ImageField('imagen', upload_to = 'imagenes/', blank = True, null = True)#metodo con el cual no es obligatorio el ingreso de datos
    caracteristicas = models.TextField(max_length = None, null = False, blank = False, verbose_name = 'Caracteristicas')
    voltage = models.IntegerField(blank = True, null = True)
    potencia = models.IntegerField(blank = True, null = True)

    class Meta:
        ordering = ["-nombre"]
        
    def __str__(self):
        return self.nombre 

    def get_filter_activities(self):   
        return self.activities_set.all()

    def get_see_parts(self):   
        return self.parts_set.all()

class Parts(models.Model):
    nombre = models.CharField(max_length = 50, null = False, blank = False)#metodo que vuelve el campo obligatorio
    equipo = models.ManyToManyField(Equipment, blank = True)
    UNIDADES = [
        ("---", '---'),
        ("CENTIMETROS", 'centimetros'),
        ("GRAMOS", 'gramos'),
        ("LITROS", 'litros'),
        ("METROS", 'metros'),
        ("UNIDADES", 'unidades'),
        ]

    unidades = models.CharField(
        max_length = 20,
        choices = UNIDADES,
        default = "---",
    )
    imagen = models.ImageField(blank = True, null = True)
    caracteristicas = models.TextField(max_length = 1500, null = False, blank = False)
    proveedor = models.CharField(max_length = 20, blank = True, null = True)
    costo = models.IntegerField(blank = True, null = True)
    SUBSISTEMA = [
        ("ELECTRICO", 'electrico'),
        ("HIDRAULICO", 'hidraulico'),
        ("NEUMATICO", 'neumatico'),
        ("CONTROL", 'control'),
        ("MECÁNICO", 'mecánico'),
        ]

    subsistema = models.CharField(
        max_length = 20,
        choices = SUBSISTEMA,
        default = "ELECTRICO",
    )

    class Meta:
        ordering = ["-nombre"]

    def __str__(self):
        return self.nombre

    def get_view_activities(self):   
        return self.activities_set.all()

class Activities(models.Model):
    nombre = models.CharField(max_length = 50, null = False, blank = False)
    equipo = models.ForeignKey(Equipment, on_delete = models.RESTRICT, blank = True, null = True)
    partes = models.ManyToManyField(Parts, through = 'PartsQuantity')   
    frecuencia = models.FloatField(null = False, blank = False)
    descripcion = models.TextField(max_length = None, null = True, blank = True)
    tiempo_estimado = models.FloatField(blank= True, null = True)
    ult_Fecha = models.DateField(auto_now_add = True)
    prox_Fecha = models.DateField(auto_now_add = True)
    anexos = models.FileField(null = True, blank = True)
    finalizado = models.BooleanField(default = False, blank = False, null = False)

    def __str__(self):
        return self.nombre + " - " + self.equipo.nombre

    class Meta:
        ordering = ["-nombre"]

    def get_filter_equipment(self):   
        return self.equipment_set.all()

class PartsQuantity(models.Model):
    parte = models.ForeignKey(Parts, null = True, blank = True, on_delete = models.CASCADE)
    actividad = models.ForeignKey(Activities, null = True, blank = True, on_delete = models.CASCADE)
    cantidad = models.FloatField(default = 1, blank = False, null = False)

class Activities_Report(models.Model):
    actividad = models.ManyToManyField(Activities, blank = True)
    inicio = models.DateTimeField(auto_now = False, auto_now_add = False, null = False, blank = False)
    fin = models.DateTimeField(auto_now = False, auto_now_add = False, null = False, blank = False)
    reporte = models.TextField(null = False, blank = False)
    responsable = models.CharField(max_length = 50, blank = True, null = True)
    costos_adicionales = models.IntegerField(blank = True, null = True)
    nota_costos = models.TextField(max_length = None, blank = True, null = True)
    imagen = models.ImageField(blank = True, null = True)
    TIPO_MANTENIMIENTO = [
        ("PREVENTIVO", 'PREVENTIVO'),
        ("CORRECTIVO", 'CORRECTIVO'),
        ]
    tipo_mantenimiento = models.CharField(
        max_length = 20,
        choices = TIPO_MANTENIMIENTO,
        default = "PREVENTIVO",
    )

    def __str__(self):
        return self.tipo_mantenimiento 

    def get_filter_rerport(self):   
        return self.rerport_set.all()
