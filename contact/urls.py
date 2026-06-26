"""
===========================================================================
URLS DE LA APLICACIÓN CONTACT (contact/urls.py)
===========================================================================

Define las rutas específicas del módulo de contacto.

Patrón: Router (enrutador)
Cada ruta asocia una URL con una vista (controlador).

Se utiliza app_name para crear un namespace, permitiendo referenciar
las URLs de forma única con {% url 'contact:<name>' %}.

Rutas públicas:
    - ''              → Formulario de contacto público

Rutas administrativas (requieren staff):
    - admin_contact/          → Panel de administración
    - admin/crear/            → Crear contacto
    - admin/<pk>/editar/      → Editar contacto
    - admin/<pk>/eliminar/    → Eliminar contacto
===========================================================================
"""

from django.urls import path
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contacto, name='contacto'),
    path('admin_contact/', views.admin_panel, name='admin_panel'),
    path('admin/crear/', views.contact_create, name='contact_create'),
    path('admin/<int:pk>/editar/', views.contact_update, name='contact_update'),
    path('admin/<int:pk>/eliminar/', views.contact_delete, name='contact_delete'),
]
