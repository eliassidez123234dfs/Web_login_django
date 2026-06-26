"""
===========================================================================
MODELOS DEL MÓDULO CONTACT (contact/models.py)
===========================================================================

Define los modelos de datos para el módulo de contacto.

Modelos:
    - Contact: Representa un mensaje de contacto enviado por un
      visitante, con nombre, correo, asunto y mensaje.
===========================================================================
"""

from django.db import models


class Contact(models.Model):
    """
    -----------------------------------------------------------------------
    Modelo: Contact

    Función
        Almacena los mensajes de contacto enviados por los visitantes
        del sitio web.

    Atributos
        nombre     : Nombre de la persona que contacta (máx. 200 caracteres).
        correo     : Correo electrónico de contacto.
        asunto     : Asunto del mensaje (máx. 300 caracteres).
        mensaje    : Cuerpo del mensaje.
        created_at : Fecha y hora de creación (automático).
        updated_at : Fecha y hora de última modificación (automático).

    Metadatos
        verbose_name        : Contacto
        verbose_name_plural : Contactos
        ordering            : -created_at (más recientes primero)
    -----------------------------------------------------------------------
    """
    nombre = models.CharField(max_length=200)
    correo = models.EmailField()
    asunto = models.CharField(max_length=300)
    mensaje = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = 'Contacto'
        verbose_name_plural = 'Contactos'
        ordering = ['-created_at']

    def __str__(self):
        return f'{self.nombre} - {self.asunto}'
