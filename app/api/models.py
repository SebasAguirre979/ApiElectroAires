from django.db import models
from django.contrib.auth.hashers import make_password

# Create your models here.
class Usuario(models.Model):
    correo = models.EmailField(unique=True)
    contrasena = models.CharField(max_length=128)
    nombre = models.CharField(max_length=255)
    celular = models.BigIntegerField()
    cedula = models.BigIntegerField()
    rol = models.CharField(max_length=10)
    def save(self, *args, **kwargs):
        self.contrasena = make_password(self.contrasena)
        super().save(*args, **kwargs)
    class Meta:
        db_table = "usuario"