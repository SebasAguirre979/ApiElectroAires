from rest_framework import serializers
from .models import Usuario

class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'

class LoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = ['correo', 'contrasena', 'nombre']