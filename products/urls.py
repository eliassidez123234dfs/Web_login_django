"""
===========================================================================
URLS DE LA APLICACIÓN PRODUCTS (products/urls.py)
===========================================================================

Define las rutas específicas del módulo de productos.

Patrón: Router (enrutador)
Cada ruta asocia una URL con una vista (controlador).

Se utiliza app_name para crear un namespace, permitiendo referenciar
las URLs de forma única con {% url 'products:<name>' %}.

Rutas públicas:
    - ''              → Catálogo de productos
    - <pk>/           → Detalle de producto

Rutas administrativas (requieren staff):
    - admin/                → Panel de administración
    - admin/crear/          → Crear producto
    - admin/<pk>/editar/    → Editar producto
    - admin/<pk>/eliminar/  → Eliminar producto
===========================================================================
"""

from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.catalogue, name='catalogue'),
    path('<int:pk>/', views.detail, name='detail'),
    path('admin/', views.admin_panel, name='admin_panel'),
    path('admin/crear/', views.producto_create, name='producto_create'),
    path('admin/<int:pk>/editar/', views.producto_update, name='producto_update'),
    path('admin/<int:pk>/eliminar/', views.producto_delete, name='producto_delete'),
]
