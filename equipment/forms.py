from django import forms

from django.forms import widgets
from .models import Equipment, Parts, Activities, Activities_Report
from tempus_dominus.widgets import DateTimePicker

class EquipmentForm(forms.ModelForm):
    class Meta:
        model = Equipment
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['imagen'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['caracteristicas'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['voltage'].widget.attrs.update({
            'class': 'form-control',
            'type':'number'
        })

        self.fields['potencia'].widget.attrs.update({
            'class': 'form-control',
            
        })

class PartsForm(forms.ModelForm):
    class Meta:
        model = Parts
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['nombre'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['equipo'].widget.attrs.update({
            'class': 'form-control', "size":10
        })

        self.fields['unidades'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['imagen'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['caracteristicas'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['proveedor'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['costo'].widget.attrs.update({
            'class': 'form-control',
        })

        self.fields['subsistema'].widget.attrs.update({
            'class': 'form-control',
        })

class ActivitiesForm(forms.Form):
    nombre=forms.CharField(max_length=50, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #equipo=forms.ModelChoiceField(queryset=Equipment.objects.all().order_by('nombre'), label='equipo', widget=forms.Select(attrs={'class':'form-control'}), required=False)
    frecuencia=forms.FloatField(label='Frecuencia (horas)', widget=forms.NumberInput(attrs={'class': 'form-control'}), required=False)
    descripcion=forms.CharField(max_length=1500, label='Descripción',
                                   widget=forms.Textarea(attrs={'class': 'form-control'}))
    tiempo_estimado=forms.FloatField(label='Tiempo estimado (h)', widget=forms.NumberInput(attrs={'class': 'form-control'}))
    ult_Fecha=forms.DateTimeField(
        label='Ultima fecha',
        widget=DateTimePicker(
            options={
                'format': 'DD/MM/YYYY HH:mm',
                'useCurrent': True,
                'collapse': True,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        )
    )
    prox_Fecha=forms.DateTimeField(
        label='Proxima fecha',
        widget=DateTimePicker(
            options={
                'format': 'DD/MM/YYYY HH:mm',
                'useCurrent': True,
                'collapse': True,
            },
            attrs={
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        )
    )
    anexos=forms.FileField(required=False)
    # finalizado = forms.BooleanField(label = 'Finalizado', required=False)

class Activities_ReportForm(forms.Form):
    actividad=forms.ModelMultipleChoiceField(queryset = Activities.objects.all().order_by('equipo'), label = 'Actividad', widget = forms.SelectMultiple(attrs = {'class':'form-control', 'size':10}), required = False)
    inicio = forms.DateTimeField(
        label = 'Fecha de inicio',
        widget = DateTimePicker(
            options = {
                'format': 'DD/MM/YYYY HH:mm',
                'useCurrent': True,
                'collapse': True,
            },
            attrs = {
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        )
    )
    fin = forms.DateTimeField(
        label = 'Fecha de fin',
        widget = DateTimePicker(
            options = {
                'format': 'DD/MM/YYYY HH:mm',
                'useCurrent': True,
                'collapse': True,
            },
            attrs = {
                'append': 'fa fa-calendar',
                'icon_toggle': True,
            }
        )
    )
    reporte = forms.CharField(max_length = 1500, label = 'Reporte',
                                   widget=forms.Textarea(attrs = {'class': 'form-control'}))
    responsable = forms.CharField(max_length = 50, label = 'Responsable',
                                   widget = forms.TextInput(attrs = {'class': 'form-control'}))
    costos_adicionales = forms.IntegerField(label = 'Costos Adicionales', widget = forms.NumberInput(attrs = {'class': 'form-control'}), required = False)
    nota_costos = forms.CharField(max_length = 500, label = 'Nota de costos',
                                   widget = forms.Textarea(attrs = {'class': 'form-control'}), required = False)
    imagen = forms.ImageField(label = 'Imagen soporte', required = False)
    TIPO_MANTENIMIENTO = [
        ("PREVENTIVO", 'Preventivo'),
        ("CORRECTIVO", 'Correctivo'),
        ]
    tipo_mantenimiento = forms.ChoiceField(choices = TIPO_MANTENIMIENTO, widget = forms.Select(attrs = {'class':'form-control'}))
