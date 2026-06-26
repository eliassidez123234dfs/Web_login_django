"""
===========================================================================
FORMULARIOS DEL MÓDULO USERS (users/forms.py)
===========================================================================

Define los formularios utilizados para la gestión de usuarios.

Patrones utilizados:
    - Formulario de Django (ModelForm y Form)
    - Validación de datos del lado del servidor
    - Personalización de widgets y etiquetas

Formularios:
    - UserRegisterForm: Para el registro de nuevos usuarios.
===========================================================================
"""

from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import RegexValidator
from django.contrib.auth.models import User

# Validador mediante expresión regular (Regex)
email_regex = RegexValidator(
    regex=r'^[\w\.-]+@[\w\.-]+\.\w+$',
    message='Ingrese un correo electrónico válido.'
)

class UserRegisterForm(UserCreationForm):
    """
    Formulario personalizado para el registro de usuarios.

    Hereda de UserCreationForm (que ya incluye username, password1 y password2).
    Añade el campo email como obligatorio.

    Validaciones:
        - Email: campo obligatorio y con formato de correo válido.
        - Username: validado por UserCreationForm (longitud, caracteres permitidos).
        - Contraseñas: deben coincidir y cumplir con los validadores configurados.
s
    Atributos Meta:
        model: User (modelo de autenticación de Django)
        fields: campos que se mostrarán en el formulario
    """

    # Campo email: obligatorio, con placeholder y clases de Bootstrap
    email = forms.EmailField(
        required=True,
        label='Correo electrónico',
        validators=[email_regex],
        widget=forms.EmailInput(
            attrs={
                'class': 'form-control',
                'placeholder': 'Correo electrónico'
            }
        )
    )

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

    def __init__(self, *args, **kwargs):
        """
        Constructor del formulario.

        Personaliza los widgets de los campos heredados (username, password1, password2)
        añadiendo clases de Bootstrap y placeholders.
        """
        super(UserRegisterForm, self).__init__(*args, **kwargs)

        # Personalizar el campo username
        self.fields['username'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Nombre de usuario'
        })
        self.fields['username'].label = 'Nombre de usuario'

        # Personalizar el campo password1
        self.fields['password1'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Contraseña'
        })
        self.fields['password1'].label = 'Contraseña'

        # Personalizar el campo password2
        self.fields['password2'].widget.attrs.update({
            'class': 'form-control',
            'placeholder': 'Confirmar contraseña'
        })
        self.fields['password2'].label = 'Confirmar contraseña'

        # Opcional: eliminar las ayudas (help_text) si son muy extensas
        # self.fields['username'].help_text = None