from estudiantes.models import Curso, Estudiante, Apoderado
from actividades.models import Actividad
from cuotas.models import Pago
from django.contrib.auth.models import User

# 1. Crear cursos
cursos_nombres = [
    "Pre-Kínder", "Kínder",
    "1° Básico", "2° Básico", "3° Básico", "4° Básico",
    "5° Básico", "6° Básico", "7° Básico", "8° Básico",
    "1° Medio", "2° Medio", "3° Medio", "4° Medio"
]

cursos = {}
for nombre in cursos_nombres:
    curso, _ = Curso.objects.get_or_create(nombre=nombre)
    cursos[nombre] = curso
    print(f"✅ Curso disponible: {nombre}")

# 2. Crear apoderados
apoderados_data = [
    {"nombre": "Marcela Soto", "rut": "12.345.678-9"},
    {"nombre": "Carlos Rivas", "rut": "13.456.789-0"},
    {"nombre": "Ana Torres", "rut": "14.567.890-1"},
    {"nombre": "Luis Herrera", "rut": "15.678.901-2"},
    {"nombre": "Patricia Díaz", "rut": "16.789.012-3"},
    {"nombre": "Jorge Pino", "rut": "17.890.123-4"},
    {"nombre": "Claudia Ramírez", "rut": "18.901.234-5"},
    {"nombre": "Rodrigo Fuentes", "rut": "19.012.345-6"},
    {"nombre": "Verónica Silva", "rut": "20.123.456-7"},
    {"nombre": "Esteban Morales", "rut": "21.234.567-8"},
]

apoderados = {}

for i, data in enumerate(apoderados_data):
    username = f"apoderado{i}"
    user, _ = User.objects.get_or_create(username=username)
    apoderado, _ = Apoderado.objects.get_or_create(
        nombre=data["nombre"],
        rut=data["rut"],
        defaults={
            "usuario": user,
            "correo": f"{username}@mail.com",
            "telefono": f"91234567{i}"
        }
    )
    apoderados[data["nombre"]] = apoderado
    print(f"👨‍👧 Apoderado creado: {data['nombre']} – {data['rut']}")

# 3. Crear estudiantes
estudiantes_data = [
    {"nombre": "Benjamín Soto", "rut": "22.345.678-0", "curso": "1° Básico", "apoderado": "Marcela Soto"},
    {"nombre": "Valentina Rivas", "rut": "22.345.678-1", "curso": "2° Básico", "apoderado": "Carlos Rivas"},
    {"nombre": "Ignacio Torres", "rut": "22.345.678-2", "curso": "3° Básico", "apoderado": "Ana Torres"},
    {"nombre": "Camila Herrera", "rut": "22.345.678-3", "curso": "4° Básico", "apoderado": "Luis Herrera"},
    {"nombre": "Matías Díaz", "rut": "22.345.678-4", "curso": "5° Básico", "apoderado": "Patricia Díaz"},
    {"nombre": "Sofía Pino", "rut": "22.345.678-5", "curso": "1° Medio", "apoderado": "Jorge Pino"},
    {"nombre": "Tomás Ramírez", "rut": "22.345.678-6", "curso": "2° Medio", "apoderado": "Claudia Ramírez"},
    {"nombre": "Isidora Fuentes", "rut": "22.345.678-7", "curso": "3° Medio", "apoderado": "Rodrigo Fuentes"},
    {"nombre": "Diego Silva", "rut": "22.345.678-8", "curso": "4° Medio", "apoderado": "Verónica Silva"},
    {"nombre": "Antonia Morales", "rut": "22.345.678-9", "curso": "Pre-Kínder", "apoderado": "Esteban Morales"},
]

for data in estudiantes_data:
    estudiante, _ = Estudiante.objects.get_or_create(
        nombre=data["nombre"],
        rut=data["rut"],
        defaults={
            "curso": cursos[data["curso"]],
            "apoderado": apoderados[data["apoderado"]]
        }
    )
    print(f"👩‍🎓 Estudiante creado: {data['nombre']} – {data['rut']} – {data['curso']}")

# 4. Crear actividades
actividades_nombres = [
    "Gala de Fin de Año", "Fiestas Patrias", "Día del Alumno",
    "Paseo Fin de Año", "Rifa Solidaria", "Campaña Solidaria",
    "Semana del Colegio", "Celebración Navidad"
]

for i, nombre in enumerate(actividades_nombres):
    curso = list(cursos.values())[i % len(cursos)]
    actividad, _ = Actividad.objects.get_or_create(
        nombre=nombre,
        curso=curso,
        defaults={
            "monto_total": 5000 + (i * 500)
        }
    )
    print(f"🎉 Actividad creada: {actividad.nombre} – ${actividad.monto_total} – Curso: {curso.nombre}")