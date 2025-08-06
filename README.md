Plataforma Web de Gestión de Cuotas Escolares

Este repositorio contiene la primera versión funcional del sistema web desarrollado como parte del proyecto de título. 
La plataforma permite registrar cuotas escolares, visualizar estados de pago y gestionar actividades académicas.

Objetivo del proyecto
Desarrollar una solución web que permita a instituciones educativas gestionar el registro y seguimiento de pagos escolares por actividad, 
con enfoque en transparencia, trazabilidad y facilidad de uso.


Tecnologías utilizadas
- Django (Python)
- SQLite
- HTML/CSS
- Git y GitHub
- Visual Studio Code


Estado actual del sistema
- Registro de cuotas: en desarrollo (formulario activo, validaciones implementadas)
- Visualización por apoderado: funcional
- Panel de estado de pagos: disponible
- Validaciones de campos: activas
- Filtros y exportación: pendientes
- Autenticación y perfiles: no implementado


Estructura del proyecto

plataformaweb/
├── actividades/              # Módulo para gestionar actividades escolares
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py

├── estudiantes/              # Módulo para gestionar estudiantes
│   ├── migrations/
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   └── views.py

├── cuotas/                   # Módulo principal para cuotas escolares
│   ├── migrations/
│   ├── templates/cuotas/
│   │   ├── panel_cuotas.html
│   │   ├── registrar_cuota.html
│   │   ├── estado_cuotas.html
│   │   └── cuotas_por_apoderado.html
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py

├── plataformaweb/            # Configuración principal del proyecto Django
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py

├── templates/                # Carpeta global de templates (si aplica)
├── static/                   # Archivos estáticos (CSS, JS, imágenes)
├── db.sqlite3                # Base de datos local
├── manage.py                 # Script principal de administración Django
├── README.md                 # Documentación del proyecto
└── .gitignore                # Exclusiones para Git


Requerimientos funcionales y porcentaje de avance
- ✅ RF01: Registrar cuotas escolares por actividad — formulario activo, validaciones implementadas
- ✅ RF02: Visualizar estado de pagos por apoderado — funcional
- ❌ RF03: Acceder al sistema con sesiones segmentadas por perfil — no implementado
- ❌ RF04: Filtrar cuotas por nombre de estudiante o actividad — pendiente
- ❌ RF05: Exportar información en PDF y Excel — pendiente
- ❌ RF06: Recibir notificaciones automáticas de nuevas cuotas y pagos pendientes — no implementado
- ✅ RF07: Validar campos obligatorios en formularios — implementado
- ❌ RF08: Visualizar mensajes y alertas según perfil — no implementado
- ⚠️ RF09: Consultar historial de cuotas vinculadas a actividades específicas — en desarrollo

Porcentaje de avance funcional estimado: 44%
Este porcentaje considera 4 de 9 requerimientos con algún grado de implementación (funcional o en desarrollo). El objetivo es alcanzar al menos un 80% de avance funcional antes del 12 de agosto, según lo solicitado por el profesor guía.


Autora
Lidia Inostroza
Proyecto de Título — Colegio Adventista Talcahuano Centro
Carrera: Ingeniería en Informática
Año: 2025



