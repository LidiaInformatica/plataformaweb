from cuotas.models import Cuota
from estudiantes.models import Estudiante
from actividades.models import Actividad
from django.shortcuts import render
from datetime import date, timedelta

def dashboard_view(request):
    recaudado = sum(c.monto_pagado for c in Cuota.objects.filter(fecha_pago__month=date.today().month))
    pendientes = Cuota.objects.filter(estado='Pendiente').count()
    alumnos = Estudiante.objects.count()
    actividades = Actividad.objects.filter(fecha__gte=date.today())
    pagos_recientes = Cuota.objects.filter(fecha_pago__gte=date.today() - timedelta(days=30)).order_by('-fecha_pago')

    context = {
        'recaudado': recaudado,
        'pendientes': pendientes,
        'alumnos': alumnos,
        'actividades': actividades,
        'pagos_recientes': pagos_recientes,
    }
    return render(request, 'core/dashboard.html', context)
