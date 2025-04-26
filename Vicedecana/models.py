from django.db import models

class Edificios(models.Model):
    numero = models.CharField(primary_key=True, max_length=255)
    facultad = models.CharField(max_length=255)
    disponibilidad = models.BooleanField(default=True)
    ano = models.CharField(max_length=255)
    carrera = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Edificio'
        verbose_name_plural = 'Edificios'

    def __str__(self):
        return str(self.numero)


class Estudiantes(models.Model):
    full_name = models.CharField(max_length=255)
    usuario = models.CharField(max_length=255)
    id = models.CharField(max_length=255, primary_key=True)
    carrera = models.CharField(max_length=255)
    facultad= models.CharField(max_length=255)
    grade = models.IntegerField()
    province = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)



    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return self.full_name