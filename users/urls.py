from django.urls import path
from . import views

"""
    Módulo de enrutamiento (Routing)

    Patrón utilizado:
    - Router: Asocia cada URL con la vista correspondiente.
    - Front Controller (implementado por Django): Todas las solicitudes HTTP
    pasan primero por el sistema de URLs antes de llegar a una vista.

    Cada llamada a path() registra una ruta que permitirá a Django despachar
    la petición a la función adecuada.
"""

"""
===========================================================================
URLS DE LA APLICACIÓN USERS (users/urls.py)
===========================================================================

Define las rutas específicas del módulo de usuarios.

Patrón: Router (enrutador)
Cada ruta asocia una URL con una vista (controlador).

Se utiliza app_name para crear un namespace, permitiendo referenciar
las URLs de forma única con {% url 'users:landing' %}.
===========================================================================
"""

from django.urls import path
from . import views

app_name = 'users'  # Namespace para evitar conflictos con otras apps

urlpatterns = [
    # Página de inicio (landing) - Raíz de la app
    path('', views.landing, name='landing'),

    # Inicio de sesión
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),

    # Registro de nuevos usuarios
    path('register/', views.registrarse, name='registrarse'),

    # Cierre de sesión
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
]
