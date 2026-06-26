from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import UserRegisterForm


"""
===========================================================================
MÓDULO DE VISTAS (views.py)
===========================================================================

Este archivo implementa la lógica de negocio del módulo de usuarios.

Patrones de diseño y principios aplicados
-----------------------------------------

• Arquitectura MVT (Model - View - Template)
  Las vistas reciben las solicitudes HTTP, procesan la información,
  interactúan con los modelos cuando es necesario y devuelven una respuesta.

• Controller
  Cada función actúa como un controlador coordinando el flujo de la petición.

• Strategy
  El comportamiento cambia dependiendo del método HTTP recibido (GET o POST).

• PRG (Post / Redirect / Get)
  Después de una operación exitosa se redirecciona al usuario para evitar
  el reenvío accidental del formulario al actualizar la página.

• Manejo de Excepciones
  Se utiliza try/except únicamente en operaciones que pueden producir errores
  inesperados, garantizando una respuesta controlada al usuario.

• Sistema de Mensajes
  Django Messages Framework informa el resultado de las operaciones
  mediante mensajes de éxito, advertencia o error.
===========================================================================
"""


def landing(request):
    """
    -----------------------------------------------------------------------
    Vista: Landing

    Función
        Mostrar la página principal del sistema.

    Patrones utilizados
        • Controller
        • MVT

    Flujo

        Usuario
            ↓
        Solicita página principal
            ↓
        Renderiza landing.html
    -----------------------------------------------------------------------
    """

    return render(request, "users/landing.html")


def registrarse(request):
    """
    -----------------------------------------------------------------------
    Vista: Registro de usuarios

    Función
        Registrar nuevos usuarios mediante UserRegisterForm.

    Patrones utilizados

        • Controller
        • Strategy (GET / POST)
        • PRG
        • Manejo de Excepciones

    Flujo

        GET
            ↓
        Mostrar formulario

        POST
            ↓
        Validar datos
            ↓
        Guardar usuario
            ↓
        Mostrar mensaje
            ↓
        Redireccionar al login
    -----------------------------------------------------------------------
    """

    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            try:

                form.save()

                messages.success(
                    request,
                    "La cuenta fue creada correctamente."
                )

                return redirect("iniciar_sesion")

            except Exception:

                messages.error(
                    request,
                    "Ocurrió un error inesperado al registrar el usuario."
                )

        else:

            messages.warning(
                request,
                "Por favor corrija los errores del formulario."
            )

    else:

        form = UserRegisterForm()

    return render(request, "users/register.html", {
        "form": form
    })


def iniciar_sesion(request):
    """
    -----------------------------------------------------------------------
    Vista: Inicio de sesión

    Función
        Autenticar usuarios registrados.

    Patrones utilizados

        • Controller
        • Strategy
        • PRG

    Flujo

        GET
            ↓
        Mostrar formulario

        POST
            ↓
        Validar credenciales
            ↓
        Autenticar usuario
            ↓
        Crear sesión
            ↓
        Redireccionar
    -----------------------------------------------------------------------
    """

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        usuario = authenticate(
            request,
            username=username,
            password=password
        )

        if usuario is not None:

            login(request, usuario)

            messages.success(
                request,
                "Bienvenido al sistema."
            )

            return redirect("landing")

        else:

            messages.error(
                request,
                "Usuario o contraseña incorrectos."
            )

    return render(request, "users/login.html")


def cerrar_sesion(request):
    """
    -----------------------------------------------------------------------
    Vista: Cierre de sesión

    Función
        Finalizar la sesión del usuario autenticado.

    Patrones utilizados

        • Controller
        • PRG

    Flujo

        Usuario
            ↓
        logout()
            ↓
        Mensaje
            ↓
        Redirección
    -----------------------------------------------------------------------
    """

    logout(request)

    messages.info(
        request,
        "La sesión fue cerrada correctamente."
    )

    return redirect("landing")

