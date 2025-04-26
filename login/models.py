from django.db import models

class Rol(models.Model):
    usuario=models.CharField(max_length=20, blank=False)
    password=models.CharField(max_length=30)


    class Meta:
        verbose_name='Rol'
        verbose_name_plural='Roles'

    def __str__(self):
        return str(self.usuario)
    

