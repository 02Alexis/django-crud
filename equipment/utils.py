from cgitb import html
from io import BytesIO
from unittest import result
from django.http import HttpResponse, request
from django.template.loader import get_template
from equipment.models import Activities, Equipment
from xhtml2pdf import pisa

def render_to_pdf(template_src, context_dic = {}):
    template = get_template(template_src)
    html = template.render(context_dic)
    result = BytesIO()
    pdf = pisa.pisaDocument(BytesIO(html.encode('ISO-8859-1')), result)
    if not pdf.err:
        return HttpResponse(result.getvalue(),content_type = 'application/pdf')
    return None

def get_or_create_actividad(id):

    actividad = Activities.objects.filter(equipo_id = id).filter(nombre = "Nueva actividad").count()
    equipo = Equipment.objects.get(id = id)
    if actividad:
        actividad = Activities.objects.filter(equipo_id = id).filter(nombre = "Nueva actividad").first()
        return actividad

    else:
        
        actividad = Activities.objects.create(nombre = "Nueva actividad",
                                                frecuencia = 3000,
                                                equipo = equipo,
                                                )
        return actividad