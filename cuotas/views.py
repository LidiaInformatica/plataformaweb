from django.shortcuts import render
from .forms import CuotaForm
from .models import Cuota
from estudiantes.models import Estudiante
from actividades.models import Actividad
from django.db.models import Sum
from datetime import date

# Vista del panel principal de cuotas (Dashboard de cuotas)
def panel_cuotas_view(request):
    ultimos_pagos = Cuota.objects.order_by('-fecha_pago')[:5]
    total_recaudado = Cuota.objects.filter(fecha_pago__month=date.today().month).aggregate(
        total=Sum('monto_pagado')
    )['total'] or 0
    pagos_pendientes = Cuota.objects.filter(estado_pago='pendiente').count()
    total_cuotas = Cuota.objects.count()

    context = {
        'ultimos_pagos': ultimos_pagos,
        'total_recaudado': total_recaudado,
        'pagos_pendientes': pagos_pendientes,
        'total_cuotas': total_cuotas,
    }
    return render(request, 'cuotas/panel_cuotas.html', context)

# Vista para registrar una nueva cuota
def registrar_pago_view(request):
    mensaje_exito = False
    saldo_pendiente = None
    form = CuotaForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            form.save()
            mensaje_exito = True
            form = CuotaForm()  # Limpiar formulario
        else:
            # 👇 Diagnóstico en consola
            print("Errores del formulario:", form.errors)

            estudiante_id = request.POST.get('estudiante')
            actividad_id = request.POST.get('actividad')

            try:
                estudiante = Estudiante.objects.get(pk=estudiante_id)
                actividad = Actividad.objects.get(pk=actividad_id)
                monto_total = actividad.monto_total
                cuotas_previas = Cuota.objects.filter(estudiante=estudiante, actividad=actividad)
                total_pagado = cuotas_previas.aggregate(Sum('monto_pagado'))['monto_pagado__sum'] or 0
                saldo_pendiente = monto_total - total_pagado
            except (Estudiante.DoesNotExist, Actividad.DoesNotExist, ValueError):
                saldo_pendiente = None

    return render(request, 'cuotas/registrar_cuota.html', {
        'form': form,
        'mensaje_exito': mensaje_exito,
        'saldo_pendiente': saldo_pendiente
    })

# Vista para mostrar estado de pagos con filtros
def estado_pagos_view(request):
    cuotas = Cuota.objects.select_related('estudiante', 'actividad')
    for cuota in cuotas:
        cuota.saldo_pendiente = cuota.actividad.monto_total - cuota.monto_pagado
    return render(request, 'cuotas/estado_cuotas.html', {'pagos': cuotas})

# Vista simulada para cuotas por apoderado (sin login)
def pagos_por_apoderado_view(request):
    apoderado_id = 1  # Simulación sin login
    estudiantes = Estudiante.objects.filter(apoderado_id=apoderado_id)
    cuotas = Cuota.objects.filter(estudiante__in=estudiantes)

    context = {
        'pagos': cuotas
    }
    return render(request, 'cuotas/cuotas_por_apoderado.html', context)

