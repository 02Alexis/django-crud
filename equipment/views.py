from dataclasses import fields
from email.mime import application
from re import template
from urllib.request import Request

from django.forms import inlineformset_factory
from .utils import render_to_pdf, get_or_create_actividad
from django.shortcuts import redirect, render, get_object_or_404
from django.http import Http404, HttpResponse
from datetime import timedelta

from django.contrib import messages  # antes de retornar
from django.contrib.messages.views import SuccessMessageMixin

from django.template import context
from django.db.models import Q
from django.core.paginator import Paginator
from django.views import View
from django.views.generic import View

from equipment.utils import render_to_pdf
from .models import Equipment, Parts, Activities, PartsQuantity, Activities_Report
from .forms import EquipmentForm, PartsForm, ActivitiesForm, Activities_ReportForm

# Create your views here.

#################################### PROXIMAS ACTIVIDADES ####################################
def home(request):
    busqueda = request.GET.get("buscar")
    actividades = Activities.objects.all().order_by('prox_Fecha')
    for actividad in actividades:
        actividad.cantidad_partes = PartsQuantity.objects.filter(actividad = actividad).order_by('-cantidad')

    if busqueda:
        actividades = Activities.objects.filter(
            Q(nombre__icontains = busqueda)
        ).order_by('nombre')

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(actividades, 10)
        actividades = paginator.page(page)
    except:
        raise Http404   
    return render(request, 'prox_actividades/home.html', {'actividades': actividades,
                                                            'paginator': paginator})

#################################### EQUIPOS ####################################

def equipos(request):
    busqueda = request.GET.get("buscar")
    equipment = Equipment.objects.all().order_by('nombre')

    if busqueda:
        equipment = Equipment.objects.filter(
            Q(nombre__icontains = busqueda)
        ).order_by('nombre')

    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(equipment, 10)
        equipment = paginator.page(page)
    except:
        raise Http404

    if request.method=='POST' and 'edit_activity' in request.POST:
        return redirect('editar_actividades', id=request.POST["select_activity"])
    if request.method=='POST' and 'edit_part' in request.POST:
        return redirect('editar_partes', id=request.POST["select_part"])
        
    return render(request, 'relaciones/index.html', {'equipment': equipment,
                                                     'paginator': paginator})

def crear(request):
    formulario = EquipmentForm()
    if request.method == 'POST':
        formulario = EquipmentForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Equipo registrado")
            return redirect('equipos')
    return render(request, 'relaciones/crear.html', {'formulario': formulario})

def detalle(request, id):
    equipment = get_object_or_404(Equipment, id = id)
    context = {
        'equipment': equipment
    }
   
    return render(request, 'relaciones/detalle.html', context)

def editar(request, id):
    equipment = Equipment.objects.get(id = id)
    formulario = EquipmentForm(instance = equipment)
    if request.method == 'POST':
        formulario = EquipmentForm(
            request.POST, request.FILES, instance = equipment)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Actualiado Correctamente')
            return redirect('equipos')
    return render(request, 'relaciones/editar.html', {'formulario': formulario})

def eliminar(request, id):
    equipments = Equipment.objects.get(id=id)
    equipments.delete()
    messages.success(request, "eliminado correctamente")
    return redirect('equipos')

############################# PARTES ####################################

def partes(request):
    busqueda = request.GET.get("buscar")
    partes = Parts.objects.all().order_by('nombre')

    if busqueda:
        partes = Parts.objects.filter(
            Q(nombre__icontains = busqueda)
        ).order_by('nombre')

    for parte in partes:
        parte.cantidad_parte = PartsQuantity.objects.filter(parte = parte)
    
    return render(request, 'partes/partes.html', {'partes': partes})

def detail_part(request, id):
    partes = get_object_or_404(Parts, id = id)
    context = {
        'partes': partes
    }
    return render(request, 'partes/detalle.html', context)

def crear_partes(request):
    formulario = PartsForm()
    if request.method == 'POST':
        formulario = PartsForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, 'Creado correctamente.')
            return redirect('partes')
    return render(request, 'partes/crear.html', {'formulario': formulario})

def anadir_parte(request, id):
    equipo = Equipment.objects.get(id = id)
    formulario = PartsForm(initial = {'equipo': equipo})
    if request.method == 'POST':
        formulario = PartsForm(request.POST, request.FILES)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "Creado Correctamente")
            return redirect('partes')
    return render(request, 'partes/crear.html', {'formulario': formulario})

def editar_partes(request, id):
    parte = Parts.objects.get(id = id)
    formulario = PartsForm(instance = parte)
    if request.method == 'POST':
        formulario = PartsForm(request.POST, request.FILES, instance = parte)
        if formulario.is_valid():
            formulario.save()
            messages.success(request, "modificado correctamente")
            return redirect('partes')
    return render(request, 'partes/editar.html', {'formulario': formulario})

def eliminar_partes(request, id):
    partes = Parts.objects.get(id=id)
    partes.delete()
    messages.success(request, "eliminado correctamente")
    return redirect('partes')

############################# ACTIVIDADES ####################################

def actividades(request):
    busqueda = request.GET.get("buscar")
    
    actividades = Activities.objects.all().order_by('nombre')

    for actividad in actividades:
        # actividad.tiempo_correctivos = reportes.objects.filter(tipo_mantenimiento="CORRECTIVO")
        # actividad.tiempo_preventivos = reportes.objects.filter(tipo_mantenimiento="PREVENTIVO")
        actividad.cantidad_partes = PartsQuantity.objects.filter(actividad = actividad).order_by('-cantidad')

    if busqueda:
        actividades = Activities.objects.filter(
            Q(nombre__icontains = busqueda)
        ).order_by('nombre')
    page = request.GET.get('page', 1)

    try:
        paginator = Paginator(actividades, 10)
        actividades = paginator.page(page)
    except:
        raise Http404        
    return render(request, 'actividades/inicio.html', {'actividades': actividades,
                                                        'paginator': paginator})

def detail_activity(request, id):
    actividades = get_object_or_404(Activities, id = id)
    context = {
        'actividades': actividades
    }
    return render(request, 'actividades/detail.html', context)

def detalle_actividad(request, id):
    reportes = Activities_Report.objects.filter(actividad_id = id)

    correctivos = reportes.filter(tipo_mantenimiento = "CORRECTIVO")
    preventivos = reportes.filter(tipo_mantenimiento = "PREVENTIVO")

    total_correctivos = correctivos.count()
    total_preventivos = preventivos.count()

    tiempo_correctivo = 0
    tiempo_preventivo = 0

    for reporte in correctivos:

        reporte.tiempo_total = (
            reporte.fin - reporte.inicio).total_seconds()/3600
        tiempo_correctivo += tiempo_correctivo + reporte.tiempo_total

    for reporte in preventivos:

        reporte.tiempo_total = (
            reporte.fin - reporte.inicio).total_seconds()/3600
        tiempo_preventivo += tiempo_preventivo + reporte.tiempo_total

    return render(request, 'actividades/detalle.html',  {'reportes': reportes,
                                                         'correctivos': correctivos,
                                                         'preventivos': preventivos,
                                                         'tiempo_correctivo': tiempo_correctivo,
                                                         'tiempo_preventivo': tiempo_preventivo})

def anadir_actividad(request, id):
    equipo = Equipment.objects.get(id = id)
    actividad = get_or_create_actividad(id)

    formulario = ActivitiesForm(initial = {'partes': partes})

    PartesFormset = inlineformset_factory(Activities, PartsQuantity,
                                            fields = ('parte','cantidad'),
                                            extra = 4,
                                            can_delete=False
                                            )

    partes_formset = PartesFormset(instance = actividad)

    for part_form in partes_formset.forms:
        part_form.fields['parte'].queryset = Parts.objects.filter(equipo = equipo)

    if request.method == 'POST':
        formulario = ActivitiesForm(request.POST, request.FILES)
        

        if formulario.is_valid():

            actividad.nombre = formulario.cleaned_data['nombre']
            actividad.frecuencia = formulario.cleaned_data['frecuencia']
            actividad.descripcion = formulario.cleaned_data['descripcion']
            actividad.tiempo_estimado = formulario.cleaned_data['tiempo_estimado']
            actividad.ult_Fecha = formulario.cleaned_data['ult_Fecha']
            actividad.prox_Fecha = formulario.cleaned_data['prox_Fecha']
            actividad.anexos = formulario.cleaned_data['anexos']
            # actividad.finalizado = formulario.cleaned_data['finalizado']
            print(actividad.id)
            actividad.save()

            
            formset = PartesFormset(request.POST, instance = actividad)
            
            if formset.is_valid():
                formset.save()
                messages.success(request, "Equipo registrado en actividad")
                return redirect('actividades')

            else:
                print("ERRORES", formset.errors)

    return render(request, 'actividades/crear.html', {'formulario': formulario,
                                                'equipo':equipo,
                                                'partes_formset':partes_formset})

def editar_actividades(request, id):
    actividad = Activities.objects.get(id = id)
    formulario = ActivitiesForm(initial = {'nombre': actividad.nombre,
                                         'partes': actividad.partes,
                                         'frecuencia': actividad.frecuencia,
                                         'descripcion': actividad.descripcion,
                                         'tiempo_estimado': actividad.tiempo_estimado,
                                         'ult_Fecha': actividad.ult_Fecha,
                                         'prox_Fecha': actividad.prox_Fecha,
                                         'anexos': actividad.anexos,
                                        #  'finalizado': actividad.finalizado,
                                         })

    PartesFormset = inlineformset_factory(Activities, PartsQuantity,
                                            fields = ('parte','cantidad'),
                                            extra = 4,
                                            )

    partes_formset = PartesFormset(instance = actividad)

    if request.method == 'POST':
        formulario = ActivitiesForm(request.POST, request.FILES)
        
    
        if formulario.is_valid():

            actividad.nombre = formulario.cleaned_data['nombre']
            actividad.frecuencia = formulario.cleaned_data['frecuencia']
            actividad.descripcion = formulario.cleaned_data['descripcion']
            actividad.tiempo_estimado = formulario.cleaned_data['tiempo_estimado']
            actividad.ult_Fecha = formulario.cleaned_data['ult_Fecha']
            actividad.prox_Fecha = formulario.cleaned_data['prox_Fecha']
            actividad.anexos = formulario.cleaned_data['anexos']
            # actividad.finalizado = formulario.cleaned_data['finalizado']
            print(actividad.id)
            actividad.save()

            
            formset = PartesFormset(request.POST, instance = actividad)

            if formset.is_valid():
                formset.save()
            messages.success(request, 'Actualiado Correctamente')
            return redirect('actividades')

        else:
            print('Errores', formulario.errors)
    return render(request, 'actividades/editar.html', {'formulario': formulario,
                                                'actividad':actividad,
                                                'partes_formset':partes_formset})

def eliminar_actividades(request, id):
    actividades = Activities.objects.get(id = id)
    actividades.delete()
    messages.success(request, "eliminado correctamente")
    return redirect('actividades')

############################# REPORTE_ACTIVIDADES ####################################

def reporte(request):
    busqueda = request.GET.get("buscar")
    
    if busqueda:
        actividades = Activities.objects.filter(nombre__icontains=busqueda)
        reportes = Activities_Report.objects.filter(
            Q(actividad__in = actividades)
        ).order_by('-id')
    else:
        reportes = Activities_Report.objects.all().order_by('-id')

    return render(request, 'reporte/inicio.html', {'reportes': reportes})

def detalle_reporte(request, id):
    reporte = get_object_or_404(Activities_Report, id = id)
    context = {
        'reporte': reporte
    }
    return render(request, 'reporte/detalle.html', context)

def anadir_reporte(request, id):
    actividad = Activities.objects.get(id = id)
    formulario = Activities_ReportForm(initial = {'actividad': actividad})
    if request.method == 'POST':
        formulario = Activities_ReportForm(request.POST, request.FILES)
        if formulario.is_valid():
            reporte = Activities_Report.objects.create(inicio = formulario.cleaned_data['inicio'],
                                                fin = formulario.cleaned_data['fin'],
                                                reporte = formulario.cleaned_data['reporte'],
                                                responsable = formulario.cleaned_data['responsable'],
                                                costos_adicionales = formulario.cleaned_data[
                                                    'costos_adicionales'],
                                                nota_costos = formulario.cleaned_data['nota_costos'],
                                                imagen = formulario.cleaned_data['imagen'],
                                                tipo_mantenimiento = formulario.cleaned_data['tipo_mantenimiento'])

            for i in formulario.cleaned_data['actividad']:

                reporte.actividad.add(i)

            actividad.ult_Fecha = reporte.inicio
            actividad.prox_Fecha = reporte.inicio + \
                timedelta(hours = actividad.frecuencia)
            actividad.save()
            return redirect('reporte')
    return render(request, 'reporte/crear.html', {'formulario': formulario})

def crear_reporte(request):
    formulario = Activities_ReportForm()
    if request.method == 'POST':
        formulario = Activities_ReportForm(request.POST, request.FILES)
        if formulario.is_valid():
            reporte = Activities_Report.objects.create( inicio = formulario.cleaned_data['inicio'],
                                              fin = formulario.cleaned_data['fin'],
                                              reporte = formulario.cleaned_data['reporte'],
                                              responsable = formulario.cleaned_data['responsable'],
                                              costos_adicionales = formulario.cleaned_data['costos_adicionales'],
                                              nota_costos = formulario.cleaned_data['nota_costos'],
                                              imagen = formulario.cleaned_data['imagen'],
                                              tipo_mantenimiento = formulario.cleaned_data['tipo_mantenimiento'])

            for i in formulario.cleaned_data['actividad']:

                reporte.actividad.add(i)

            reporte.save()
            messages.success(request, 'Creado Correctamente')
            return redirect('reporte')
        else:
            print("Errores", formulario.errors)

    return render(request, 'reporte/crear.html', {'formulario': formulario})

def editar_reporte(request, id):
    reporte = Activities_Report.objects.get(id = id)
    formulario = Activities_ReportForm(initial = {'actividad': reporte.actividad.all(),
                                                 'inicio': reporte.inicio,
                                                 'fin': reporte.fin,
                                                 'reporte': reporte.reporte,
                                                 'responsable': reporte.responsable,
                                                 'costos_adicionales': reporte.costos_adicionales,
                                                 'nota_costos': reporte.nota_costos,
                                                 'imagen': reporte.imagen,
                                                 'tipo_mantenimiento': reporte.tipo_mantenimiento,
                                                 })
    if request.method == 'POST':
        formulario = Activities_ReportForm(request.POST, request.FILES)

        if formulario.is_valid():
            actividades = formulario.cleaned_data['actividad']
            reporte.actividad.set(actividades)

            reporte.inicio = formulario.cleaned_data['inicio']
            reporte.fin = formulario.cleaned_data['fin']
            reporte.reporte = formulario.cleaned_data['reporte']
            reporte.responsable = formulario.cleaned_data['responsable']
            reporte.costos_adicionales = formulario.cleaned_data['costos_adicionales']
            reporte.nota_costos = formulario.cleaned_data['nota_costos']
            reporte.tipo_mantenimiento = formulario.cleaned_data['tipo_mantenimiento']

            if formulario.cleaned_data['imagen']:
                reporte.imagen = formulario.cleaned_data['imagen']

        

            reporte.save()
            messages.success(request, 'Se cambió correctamente.')
        else:
            print('Errores', formulario.errors)

        return redirect('reporte')

    return render(request, 'reporte/editar.html', {'formulario': formulario, 'reporte':reporte})

def eliminar_reporte(request, id):
    reporte = Activities_Report.objects.get(id = id)
    reporte.delete()
    messages.success(request, "eliminado correctamente")
    return redirect('reporte')

class generar_reporte_actividades(View):
    def get(self, request, *args, **kwargs):
        template_name = "reporte/reporte_actividad.html"
        reporte = Activities_Report.objects.all()
        data = {
            'count': reporte.count(),
            'reportes': reporte
        }
        pdf = render_to_pdf(template_name, data)
        return HttpResponse(pdf, content_type = 'application/pdf')
