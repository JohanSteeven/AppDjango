from django.db import models

class Tarea(models.Model):
    PRIORIDAD_CHOICES = [
        ('Baja', 'Baja'),
        ('Media', 'Media'),
        ('Alta', 'Alta'),
    ]

    titulo = models.CharField(max_length=200, verbose_name="Título")
    descripcion = models.TextField(verbose_name="Descripción")
    fecha_entrega = models.DateField(verbose_name="Fecha de Entrega")
    prioridad = models.CharField(max_length=10, choices=PRIORIDAD_CHOICES, default='Media', verbose_name="Prioridad")
    completada = models.BooleanField(default=False, verbose_name="Completada")
    fecha_creacion = models.DateTimeField(auto_now_add=True, verbose_name="Fecha de Creación")

    def __str__(self):
        return self.titulo
