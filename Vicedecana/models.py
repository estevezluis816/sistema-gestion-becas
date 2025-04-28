from django.db import models

class Edificios(models.Model):
    numero = models.CharField(primary_key=True, max_length=255)  # Si el número de edificio es alfanumérico
    facultad = models.CharField(max_length=255)
    disponibilidad = models.BooleanField(default=True)
    ano = models.CharField(max_length=255)
    carrera = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Edificio'
        verbose_name_plural = 'Edificios'

    def __str__(self):
        return f"Edificio {self.numero}"

class Apartamento(models.Model):
    numero = models.CharField(max_length=10)  # Número de apartamento: Ej: "101", "102", etc.
    edificio = models.ForeignKey(Edificios, on_delete=models.CASCADE, related_name="apartamentos")
    disponibilidad = models.BooleanField(default=True)

    class Meta:
        verbose_name = 'Apartamento'
        verbose_name_plural = 'Apartamentos'
        unique_together = ('numero', 'edificio')  # Asegura que el número de apartamento sea único por edificio

    def __str__(self):
        return f"Apartamento {self.numero} - Edificio {self.edificio.numero}"

    def cambiar_disponibilidad(self):
        """Método para cambiar la disponibilidad del apartamento."""
        self.disponibilidad = not self.disponibilidad
        self.save()

class Estudiantes(models.Model):
    full_name = models.CharField(max_length=255)
    usuario = models.CharField(max_length=255)
    id = models.CharField(max_length=255, primary_key=True)  # Si 'id' es único, está bien como primary_key
    carrera = models.CharField(max_length=255)
    facultad = models.CharField(max_length=255)
    grade = models.IntegerField()
    province = models.CharField(max_length=255)
    municipio = models.CharField(max_length=255)
    apartamento = models.ForeignKey(Apartamento, on_delete=models.SET_NULL, null=True, blank=True)

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'

    def __str__(self):
        return self.full_name

    def asignar_apartamento(self, apartamento):
        """Método para asignar un apartamento a un estudiante."""
        if apartamento and apartamento.disponibilidad:
            self.apartamento = apartamento
            apartamento.cambiar_disponibilidad()  # Cambia la disponibilidad del apartamento
            self.save()
        else:
            raise ValueError("El apartamento no está disponible.")
