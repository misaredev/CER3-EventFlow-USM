from django.db import models


TIPO = (
    ('V', 'Vacaciones'),
    ('F', 'Feriado'),
    ('S', 'Suspensión de actividades'),
    ('SPM', 'Suspensión de actividades PM'),
    ('P', 'Periodo Lectivo'),
    ('SE', 'Suspensión de evaluaciones'),
    ('C', 'Ceremonia'),
    ('E', 'EDDA'),
    ('EV', 'Evaluación'),
    ('A', 'Ayudantías'),
    ('H', 'Hito académico'),
    ('SA', 'Secretaría Académica'),
    ('O', 'OAI'),
)

class Segmento(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre

class Evento(models.Model):
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    titulo = models.CharField(max_length=100)
    descripcion = models.CharField(max_length=500)
    tipo = models.CharField(max_length=20, choices=TIPO, default="V")
    segmentos = models.ManyToManyField('segmento')

    def __str__(self):
        return self.titulo
