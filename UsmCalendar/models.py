from django.db import models

# Create your models here.

tipo = (
    ('V', 'Vacaciones'),
    ('F', 'Feriado'),
    ('S', 'Suspension de actividades'),
    ('SPM', 'Suspension de actividades PM'),
    ('P', 'Periodo Lectivo'),
    ('SE', 'Suspension de evaluaciones'),
    ('C', 'Ceremonia'),
    ('E', 'EDDA'),
    ('EV', 'Evaluación'),
    ('A', 'Ayudantías'),
    ('H', 'Hito académico'),
    ('SA', 'Secretaria Académica'),
    ('O', 'OAI'),
)
segmento = (('1','comunidad USM'),('2', 'Estudiantes'),('3', 'Profesor'),('4', 'jefe de carrera '),)

class Evento(models.Model):
    fecha_inicio = models.DateField()
    fecha_termino = models.DateField()
    titulo = models.CharField(max_length = 100)
    descripcion = models.CharField(max_length=500)
    tipo = models.CharField(max_length = 20,choices = tipo, default="V")
    segmentos = models.ManyToManyField('segmento')

    def __str__(self):
        return self.titulo

class Segmento(models.Model):
    nombre = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return self.nombre