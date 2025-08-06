from django.db import models
from estudiantes.models import Curso
# Importa el modelo Curso

class Actividad(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    fecha = models.DateField()
    monto_total = models.DecimalField(max_digits=10, decimal_places=2)

    curso = models.ForeignKey(
        Curso,
        on_delete=models.CASCADE,
        related_name='actividades_generales',  # ← cambiado para evitar conflicto
        null=True,
        blank=True,
        help_text="Curso al que está asociada la actividad"
    )

    def __str__(self):
        monto_formateado = f"${self.monto_total:,.0f}".replace(",", ".")  # ← formato chileno sin decimales
        curso_nombre = self.curso.nombre if self.curso else "Sin curso"
        return f"{self.nombre} – {monto_formateado} – {curso_nombre}"

