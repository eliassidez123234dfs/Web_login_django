"""
===========================================================================
ADMINISTRACIÓN DEL MÓDULO PRODUCTS (products/admin.py)
===========================================================================

Configura la interfaz de administración de Django para los modelos
del módulo de productos.

Modelos registrados:
    - Producto: Visualización en lista con filtros y búsqueda.
===========================================================================
"""

from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    """
    -----------------------------------------------------------------------
    Admin: ProductoAdmin

    Función
        Configura la visualización y gestión de productos en el
        panel de administración de Django.

    Atributos
        list_display : nombre, precio, disponible, created_at
        list_filter  : disponible, created_at
        search_fields: nombre, descripcion
        ordering     : -created_at
    -----------------------------------------------------------------------
    """
    list_display = ['nombre', 'precio', 'disponible', 'created_at']
    list_filter = ['disponible', 'created_at']
    search_fields = ['nombre', 'descripcion']
    ordering = ['-created_at']
