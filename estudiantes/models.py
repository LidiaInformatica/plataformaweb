from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Apoderado(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    telefono = models.CharField(max_length=20)
    correo = models.EmailField()

    def __str__(self):
        return self.nombre

class Estudiante(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    apoderado = models.ForeignKey(Apoderado, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre

class Directiva(models.Model):
    nombre = models.CharField(max_length=100)
    rut = models.CharField(max_length=12, unique=True)
    cargo = models.CharField(max_length=100)
    correo = models.EmailField()

    def __str__(self):
        return f"{self.cargo} - {self.nombre}"

class ActividadEscolar(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    fecha = models.DateField()
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE, related_name='actividades_escolares')

    def __str__(self):
        return f"{self.nombre} ({self.curso})"