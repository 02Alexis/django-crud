from typing import List
from django.contrib import admin

from import_export import resources
from import_export.admin import ImportExportModelAdmin

# Register your models here.

from equipment .models import Equipment, Parts, Activities, Activities_Report, PartsQuantity




#######################class Equipment
class EquipmentResource(resources.ModelResource):
    class Meta:
        model = Activities

class EquipmentAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = (EquipmentResource)
    list_display=("nombre", "caracteristicas")
    fields = ["nombre", "imagen", "caracteristicas", ('voltage', 'potencia')] #se enlista horizontalmente las encerradas en una tupla


admin.site.register(Equipment, EquipmentAdmin)

#######################class Parts
class PartsAdmin(admin.ModelAdmin):
    list_display=("nombre", "costo")

admin.site.register(Parts, PartsAdmin)

#######################class Activities
class ActivitiesResource(resources.ModelResource):
    class Meta:
        model = Activities

class PartsQuantityInline(admin.TabularInline):
    list_display=("parte", "cantidad")
    model = PartsQuantity
    extra = 2

class ActivitiesAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = (ActivitiesResource)
    list_display=("nombre", "frecuencia", "ult_Fecha", "prox_Fecha")
    inlines = [PartsQuantityInline] ### añade el formulario de PartsQuantity
    list_filter = ("tiempo_estimado", "ult_Fecha")
    date_hierarchy = "prox_Fecha"
    search_fields =("nombre",)

admin.site.register(Activities, ActivitiesAdmin)

#######################class Activities_Report
class Activities_ReportResource(resources.ModelResource):
    class Meta:
        model = Activities_Report

class Activities_ReportAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    resource_class = (Activities_ReportResource)
    list_display = ("inicio", "fin",)
    list_filter = ("actividad",)
    date_hierarchy = "inicio"
    search_fields =("tipo_mantenimiento",)
    resource_class = (Activities_ReportResource)
    
admin.site.register(Activities_Report, Activities_ReportAdmin)
