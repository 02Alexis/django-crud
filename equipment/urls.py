from django import urls
from django.urls import path
from django.urls.conf import include
from . import views

from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    path('prox-actividades', views.home, name='prox_actividades'), #### URLS NEXT ACTIVITYS
    
    ####################################### URLS EQUIPMENTS
    path('', views.equipos, name='equipos'),
    path('equipo/<int:id>', views.detalle, name='detalle'),
    path('equipos/crear', views.crear, name='crear'),
    path('equipos/editar', views.editar, name='editar'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
    path('equipos/editar/<int:id>', views.editar, name='editar'),

    ####################################### URLS PARTS
    path('partes', views.partes, name='partes'),
    path('anadir/parte/<int:id>', views.anadir_parte, name='anadir_parte'),
    path('partes/crear', views.crear_partes, name='crear_partes'),
    path('detalle-parte/<int:id>', views.detail_part, name='detail_part'),
    path('partes/editar', views.editar_partes, name='editar_partes'),
    path('eliminar_partes/<int:id>', views.eliminar_partes, name='eliminar_partes'),
    path('partes/editar/<int:id>', views.editar_partes, name='editar_partes'),

    ####################################### URLS ACTIVITYS
    path('actividades', views.actividades, name='actividades'),
    path('anadir-activid/<int:id>', views.anadir_actividad, name='anadir_actividad'),
    path('actividad/<int:id>', views.detalle_actividad, name='actividad'),
    path('detalle-actividad/<int:id>', views.detail_activity, name='activity'),
    path('actividades/editar', views.editar_actividades, name='editar_actividades'),
    path('eliminar_actividades/<int:id>', views.eliminar_actividades, name='eliminar_actividades'),
    path('actividades/editar/<int:id>', views.editar_actividades, name='editar_actividades'),

    ####################################### URLS REPORTS
    path('reporte', views.reporte, name='reporte'),
    path('generar_reporte_actividades/', views.generar_reporte_actividades.as_view(), name='generar_reporte_actividades'),
    path('anadir/reporte/<int:id>', views.anadir_reporte, name='anadir_reporte'),
    path('reporte/crear', views.crear_reporte, name='crear_reporte'),
    path('detalle-reporte/<int:id>', views.detalle_reporte, name='detalle_reporte'),
    path('reporte/editar', views.editar_reporte, name='editar_reporte'),
    path('eliminar_reporte/<int:id>', views.eliminar_reporte, name='eliminar_reporte'),
    path('reporte/editar/<int:id>', views.editar_reporte, name='editar_reporte'),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    