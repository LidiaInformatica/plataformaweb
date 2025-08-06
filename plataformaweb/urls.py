from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),

    # App core: reportes, utilidades, autenticación
    path('core/', include('core.urls')),

    # App estudiantes: gestión de cursos, inscripciones, perfiles
    path('estudiantes/', include('estudiantes.urls')),

    # App cuotas: pagos, vencimientos, estados de cuenta
    path('cuotas/', include('cuotas.urls')),

    # App actividades: extracurriculares, asistencia, participación
    path('actividades/', include('actividades.urls')),
]