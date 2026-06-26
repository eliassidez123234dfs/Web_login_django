"""
===========================================================================
URLS PRINCIPALES DEL PROYECTO (core/urls.py)
===========================================================================

Este archivo define el enrutamiento global del proyecto.

Patrón utilizado: Front Controller (controlador frontal)
Todas las solicitudes HTTP entran por este archivo y se distribuyen
a las aplicaciones correspondientes mediante include().

Estructura:
    - Las rutas de administración van en /admin/
    - Las rutas de la aplicación 'users' van en la raíz ('')
      para que landing page sea la página de inicio.
===========================================================================
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    # Panel de administración de Django
    path('admin/', admin.site.urls),

    # Incluir todas las rutas de la app 'users' en la raíz del sitio
    # Esto permite que la landing page esté en '/' y no en '/landing/'
    path('', include('users.urls')),
]