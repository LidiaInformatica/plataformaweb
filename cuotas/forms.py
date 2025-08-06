from django import forms
from .models import Cuota
from estudiantes.models import Estudiante, Apoderado
from actividades.models import Actividad
from datetime import date
from django.db.models import Sum

class CuotaForm(forms.ModelForm):
    estudiante = forms.ModelChoiceField(
        queryset=Estudiante.objects.all(),
        label="Seleccione estudiante",
        widget=forms.Select(attrs={
            'class': 'form-select',
            'title': 'Seleccione el estudiante'
        })
    )

    apoderado = forms.ModelChoiceField(
        queryset=Apoderado.objects.all(),
        label="Seleccione apoderado",
        widget=forms.Select(attrs={
            'class': 'form-select',
            'title': 'Seleccione el apoderado que realiza el pago'
        })
    )

    actividad = forms.ModelChoiceField(
        queryset=Actividad.objects.all(),
        label="Seleccione actividad",
        widget=forms.Select(attrs={
            'class': 'form-select',
            'title': 'Seleccione la actividad escolar'
        })
    )

    fecha_pago = forms.DateField(
        input_formats=['%Y-%m-%d'],
        required=True,
        widget=forms.DateInput(
            format='%Y-%m-%d',
            attrs={
                'placeholder': 'AAAA-MM-DD',
                'type': 'date',
                'class': 'form-control',
                'title': 'Seleccione la fecha del pago'
            }
        )
    )

    class Meta:
        model = Cuota
        fields = [
            'estudiante',
            'apoderado',
            'actividad',
            'monto_pagado',
            'metodo_pago',
            'estado_pago',
            'fecha_pago',
            'observacion',
        ]
        widgets = {
            'monto_pagado': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Ingrese monto a pagar',
                'title': 'Monto pagado en CLP',
                'min': '0'
            }),
            'metodo_pago': forms.Select(attrs={
                'class': 'form-select',
                'title': 'Método de pago'
            }),
            'estado_pago': forms.Select(attrs={
                'class': 'form-select',
                'title': 'Seleccione el estado del pago'
            }),
            'observacion': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Observaciones adicionales',
                'rows': 2
            }),
        }

    def clean(self):
        cleaned_data = super().clean()
        estudiante = cleaned_data.get('estudiante')
        actividad = cleaned_data.get('actividad')
        monto_pagado = cleaned_data.get('monto_pagado')
        fecha_pago = cleaned_data.get('fecha_pago')

        if not monto_pagado:
            self.add_error('monto_pagado', "Debe ingresar el monto pagado.")

        if fecha_pago and fecha_pago > date.today():
            self.add_error('fecha_pago', "La fecha de pago no puede ser futura.")

        if estudiante and actividad and monto_pagado:
            monto_total = actividad.monto_total
            cuotas_previas = Cuota.objects.filter(estudiante=estudiante, actividad=actividad)
            total_pagado = cuotas_previas.aggregate(Sum('monto_pagado'))['monto_pagado__sum'] or 0
            saldo_pendiente = monto_total - total_pagado

            if monto_pagado > saldo_pendiente:
                self.add_error('monto_pagado', f"El monto ingresado excede el saldo pendiente (${saldo_pendiente}).")