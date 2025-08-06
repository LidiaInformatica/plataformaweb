from datetime import date
from django.db import models
from estudiantes.models import Estudiante
from actividades.models import Actividad

class Apoderado(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Cuota(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('pagado', 'Pagado'),
    ]

    METODO_CHOICES = [
        ('efectivo', 'Efectivo'),
        ('transferencia', 'Transferencia'),
        ('tarjeta', 'Tarjeta'),
        ('otro', 'Otro'),
    ]

    estudiante = models.ForeignKey(
        Estudiante,
        on_delete=models.CASCADE,
        related_name="cuotas"
    )

    apoderado = models.ForeignKey(
        Apoderado,
        on_delete=models.SET_NULL,
        null=True,
        related_name="cuotas"
    )

    actividad = models.ForeignKey(
        Actividad,
        on_delete=models.CASCADE,
        related_name="cuotas"
    )

    monto_pagado = models.PositiveIntegerField()

    metodo_pago = models.CharField(
        max_length=15,
        choices=METODO_CHOICES,
        default='efectivo'
    )

    estado_pago = models.CharField(
        max_length=10,
        choices=ESTADO_CHOICES,
        default='pagado'
    )

    fecha_pago = models.DateField(
        default=date.today  # ✅ Editable y con valor por defecto
    )

    observacion = models.TextField(
        blank=True,
        default="Sin observaciones"
    )

    class Meta:
        verbose_name = 'Cuota'
        verbose_name_plural = 'Cuotas'
        ordering = ['-fecha_pago']

    def __str__(self):
        return f"{self.estudiante} – {self.actividad.nombre} – ${self.monto_pagado}"