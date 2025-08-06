from django.urls import path
from . import views

app_name = 'cuotas'

urlpatterns = [
    # Ruta raíz: muestra el panel principal al visitar /cuotas/
    path('', views.panel_cuotas_view, name='panel_cuotas'),

    # Ruta alternativa explícita para el panel
    path('panel/', views.panel_cuotas_view, name='panel_cuotas'),

    # Formulario para registrar una nueva cuota
    path('registrar/', views.registrar_pago_view, name='registrar_pago'),

    # Vista para consultar estado de pagos con filtros
    path('estado/', views.estado_pagos_view, name='estado_pagos'),

    # Vista simulada para ver pagos por apoderado (sin login)
    path('apoderado/', views.pagos_por_apoderado_view, name='cuotas_por_apoderado'),
]
