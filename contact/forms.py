"""
===========================================================================
FORMULARIOS DEL MÓDULO CONTACT (contact/forms.py)
===========================================================================

Define los formularios utilizados para la gestión de mensajes de contacto.

Patrones utilizados:
    - ModelForm de Django
    - Validación de datos del lado del servidor
    - Personalización de widgets y etiquetas

Formularios:
    - FormContactUser: Para el envío y administración de mensajes.
===========================================================================
"""

from django import forms
from .models import Contact


class FormContactUser(forms.ModelForm):
    """
    -----------------------------------------------------------------------
    Formulario: FormContactUser

    Función
        Formulario basado en el modelo Contact para el envío de
        mensajes de contacto desde la vista pública y para la
        administración desde el panel del staff.

    Meta
        model  : Contact
        fields : nombre, correo, asunto, mensaje

    Widgets personalizados
        - TextInput, EmailInput, Textarea
        - Clases Bootstrap (form-control)
    -----------------------------------------------------------------------
    """
    class Meta:
        model = Contact
        fields = ['nombre', 'correo', 'asunto', 'mensaje']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'correo': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Correo electronico', 'autocomplete': 'email'}),
            'asunto': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Asunto del mensaje'}),
            'mensaje': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Ingresa un mensaje'}),
        }
        labels = {
            'nombre': 'Nombre',
            'correo': 'Correo electronico',
            'asunto': 'Asunto',
            'mensaje': 'Mensaje',
        }
