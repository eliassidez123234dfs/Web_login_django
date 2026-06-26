from django.urls import path
from . import views

"""
    Users - Landing:
        Este apartado corresponde a las urls que contiene el modulo de users.
            langing/
            login/
            logout/
            register/

"""

urlpatterns = [
    path('landing/', views.landing, name='landing'),
    path('login/', views.iniciar_sesion, name='iniciar_sesion'),
    path('register/', views.registrarse, name='registrarse'),
    path('logout/', views.cerrar_sesion, name='cerrar_sesion'),
]
