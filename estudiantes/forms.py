from django import forms
from cuotas.models import Pago
from estudiantes.models import Estudiante, Apoderado

class PagoForm(forms.ModelForm):
    estudiante = forms.ModelChoiceField(
        queryset=Estudiante.objects.none(),
        label="Seleccione estudiante",
        widget=forms.Select(attrs={
            'class': 'form-select',
            'title': 'Seleccione el estudiante'
        })
    )

    apoderado = forms.ModelChoiceField(
        queryset=Apoderado.objects.none(),
        label="Seleccione apoderado",
        widget=forms.Select(attrs={
            'class': 'form-select',
            'title': 'Seleccione el apoderado que realiza el pago'
        })
    )