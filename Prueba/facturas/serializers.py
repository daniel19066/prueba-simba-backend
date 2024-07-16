from django.contrib.auth.models import Group, User
from rest_framework import serializers
from .models import Empresa, Clientes, DetFactura, MaeFactura, Productos

class EmpresaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Empresa
        fields = '__all__'

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clientes
        fields = '__all__'

class DetFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = DetFactura
        fields = '__all__'

class MaeFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = MaeFactura
        fields = '__all__'

class ProductoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Productos
        fields = '__all__'

