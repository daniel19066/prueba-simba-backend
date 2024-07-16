from rest_framework import viewsets
from .models import Empresa, Clientes,DetFactura,MaeFactura,Productos
from .serializers import EmpresaSerializer ,ClienteSerializer, DetFacturaSerializer, MaeFacturaSerializer, ProductoSerializer

class EmpresaViewSet(viewsets.ModelViewSet):
    queryset = Empresa.objects.all()
    serializer_class = EmpresaSerializer

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Clientes.objects.all()
    serializer_class = ClienteSerializer

class DetFacturaViewSet(viewsets.ModelViewSet):
    queryset = DetFactura.objects.all()
    serializer_class = DetFacturaSerializer

class MaeFacturaViewSet(viewsets.ModelViewSet):
    queryset = MaeFactura.objects.all()
    serializer_class = MaeFacturaSerializer

class ProductoViewSet(viewsets.ModelViewSet):
    queryset = Productos.objects.all()
    serializer_class = ProductoSerializer