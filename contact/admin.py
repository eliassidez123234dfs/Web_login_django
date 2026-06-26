"""
===========================================================================
ADMINISTRACIÓN DEL MÓDULO CONTACT (contact/admin.py)
===========================================================================

Configura la interfaz de administración de Django para los modelos
del módulo de contacto.

Modelos registrados:
    - Contact: Visualización en lista de mensajes recibidos.
===========================================================================
"""

from django.contrib import admin
from .models import Contact


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    """
    -----------------------------------------------------------------------
    Admin: ContactAdmin

    Función
        Configura la visualización y gestión de mensajes de contacto
        en el panel de administración de Django.

    Atributos
        list_display : nombre, correo, asunto, created_at
        list_filter  : created_at
        search_fields: nombre, correo, asunto
        ordering     : -created_at
    -----------------------------------------------------------------------
    """
    list_display = ['nombre', 'correo', 'asunto', 'created_at']
    list_filter = ['created_at']
    search_fields = ['nombre', 'correo', 'asunto']
    ordering = ['-created_at']
