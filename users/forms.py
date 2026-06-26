from django.forms import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(label="", widget=forms.EmailInput(attrs={'placeholder': 'Correo electronico'}))
    first_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Nombre'}))
    last_name = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder': 'Apellido'}))

    class Meta:
        model = User # Traemos el modelo de usuarios dado desde Django
        fields = ['username', 'email', 'first_name', 'last_name', 'password1', 'password2']

    "Patron Creacional: Personalizar dinamica con __init__ "
    def __init__(self, *args, **kwargs):
        super(UserRegisterForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs['class'] = 'form-control' # widget=como se vera el campo en html attrs significa: atributos de HTML adicionales
        self.fields['username'].widget.attrs['placeholder'] = 'Nombre de usuario' # Buscamos el campo username y agregamos un archivo HTML placeholder
        self.fields['username'].label=''
        self.fields['username'].help_text = ('<span class="form-text text-muted">Requerido . 150 caracteres o menos. Letras, digitos y @/ ./ +/-/_ solamente </span>')

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Contraseña'
        self.fields['password1'].label=''
        self.fields['password1'].help_text = ('<ul class=""> <li>Tu contraseña no puede ser demasiado similar a tu otra información personal.</li> <li>Tu contraseña debe contener al menos 8 caracteres.</li> <li>Tu contraseña no puede ser una contraseña común.</li> <li>Tu contraseña no puede ser completamente numérica.</li> </ul>')

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmar contraseña'
        self.fields['password2'].label=''
        self.fields['password2'].help_text = ('<span class="form-text"> Las contraseñas deben coincidir </span>')

            
            