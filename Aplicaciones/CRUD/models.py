from django.db import models

# Create your models here.
class Usuario(models.Model):
    codigo = models.CharField(primary_key=True, max_length=6)
    usuario = models.CharField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        texto = "{0} ({1})"
        return texto.format(self.usuario,  self.password)