"""
URL configuration for Prueba project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from facturas.views import EmpresaViewSet, ClienteViewSet, DetFacturaViewSet, MaeFacturaViewSet, ProductoViewSet

router = routers.DefaultRouter()
router.register(r'empresas', EmpresaViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'detFactura', DetFacturaViewSet)
router.register(r'maeFactura', MaeFacturaViewSet)
router.register(r'productos', ProductoViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
     path('', include(router.urls)),
]
