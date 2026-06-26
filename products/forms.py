"""
===========================================================================
FORMULARIOS DEL MÓDULO PRODUCTS (products/forms.py)
===========================================================================

Define los formularios utilizados para la gestión de productos.

Patrones utilizados:
    - ModelForm de Django
    - Validación de datos del lado del servidor
    - Personalización de widgets y etiquetas

Formularios:
    - ProductoForm: Para la creación y edición de productos.
===========================================================================
"""

from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    """
    -----------------------------------------------------------------------
    Formulario: ProductoForm

    Función
        Formulario basado en el modelo Producto para crear y editar
        productos desde el panel de administración.

    Meta
        model  : Producto
        fields : nombre, descripcion, precio, imagen, disponible

    Widgets personalizados
        - TextInput, Textarea, NumberInput, FileInput, CheckboxInput
        - Clases Bootstrap (form-control, form-check-input)
    -----------------------------------------------------------------------
    """
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'imagen', 'disponible']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nombre del producto'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Descripción del producto', 'rows': 4}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': '0.00'}),
            'imagen': forms.FileInput(attrs={'class': 'form-control'}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
        labels = {
            'nombre': 'Nombre',
            'descripcion': 'Descripción',
            'precio': 'Precio',
            'imagen': 'Imagen del producto',
            'disponible': 'Disponible para la venta',
        }
