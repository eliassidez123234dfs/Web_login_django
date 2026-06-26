"""
===========================================================================
MODELOS DEL MÓDULO PRODUCTS (products/models.py)
===========================================================================

Define los modelos de datos para el catálogo de productos.

Modelos:
    - Producto: Representa un producto del catálogo con nombre,
      descripción, precio, imagen y estado de disponibilidad.
===========================================================================
"""

from django.db import models


class Producto(models.Model):
    """
    -----------------------------------------------------------------------
    Modelo: Producto

    Función
        Representa un producto dentro del catálogo del sistema.

    Atributos
        nombre       : Nombre del producto (máx. 200 caracteres).
        descripcion  : Descripción detallada del producto (opcional).
        precio       : Precio del producto con hasta 10 dígitos y 2 decimales.
        imagen       : Imagen del producto (opcional, se almacena en media/).
        disponible   : Indica si el producto está disponible para la venta.
        created_at   : Fecha y hora de creación (automático).
        updated_at   : Fecha y hora de última modificación (automático).

    Metadatos
        verbose_name        : Producto
        verbose_name_plural : Productos
        ordering            : -created_at (más recientes primero)
    -----------------------------------------------------------------------
    """
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    imagen = models.ImageField(upload_to='productos/', blank=True, null=True)
    disponible = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        ordering = ['-created_at']

    def __str__(self):
        return self.nombre
