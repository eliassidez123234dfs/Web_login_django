"""
===========================================================================
MÓDULO DE VISTAS (contact/views.py)
===========================================================================

Este archivo implementa la lógica de negocio del módulo de contacto.

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

• Restricción de acceso por decorador
  Las vistas de administración usan @staff_member_required para restringir
  el acceso exclusivamente a usuarios del staff.

• Sistema de Mensajes
  Django Messages Framework informa el resultado de las operaciones
  mediante mensajes de éxito.

• Notificación por correo electrónico
  Cuando un usuario envía un mensaje de contacto, se envía una notificación
  al correo configurado en CONTACT_EMAIL.
===========================================================================
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Contact
from .forms import FormContactUser


def contacto(request):
    """
    -----------------------------------------------------------------------
    Vista: Formulario de contacto público

    Función
        Mostrar el formulario de contacto público y procesar el envío
        de mensajes por parte de los visitantes.

    Patrones utilizados
        • Controller
        • Strategy (GET / POST)
        • PRG
        • Notificación por correo

    Flujo

        GET
            ↓
        Mostrar formulario vacío

        POST
            ↓
        Validar datos del formulario
            ↓
        Guardar mensaje en la base de datos
            ↓
        Enviar notificación por correo al administrador
            ↓
        Mensaje de éxito
            ↓
        Redireccionar a la misma página
    -----------------------------------------------------------------------
    """
    if request.method == 'POST':
        form = FormContactUser(request.POST)
        if form.is_valid():
            contacto = form.save()

            asunto = f'Nuevo mensaje de contacto: {contacto.asunto}'
            mensaje = (
                f'Nombre: {contacto.nombre}\n'
                f'Correo: {contacto.correo}\n'
                f'Asunto: {contacto.asunto}\n\n'
                f'Mensaje:\n{contacto.mensaje}'
            )

            try:
                send_mail(
                    asunto,
                    mensaje,
                    settings.DEFAULT_FROM_EMAIL,
                    [settings.CONTACT_EMAIL],
                    fail_silently=False,
                )
            except Exception:
                pass

            messages.success(request, 'Mensaje enviado correctamente. Nos pondremos en contacto pronto.')
            return redirect('contact:contacto')
    else:
        form = FormContactUser()
    return render(request, 'contact/contacto.html', {'form': form})


@staff_member_required
def admin_panel(request):
    """
    -----------------------------------------------------------------------
    Vista: Panel de administración de contactos

    Función
        Listar todos los mensajes de contacto recibidos para su
        gestión por parte del staff.

    Patrones utilizados
        • Controller
        • MVT
        • Restricción de acceso

    Flujo

        Staff
            ↓
        Solicita panel de administración
            ↓
        Obtiene todos los mensajes de contacto
            ↓
        Renderiza admin_panel.html con los contactos
    -----------------------------------------------------------------------
    """
    contacto = Contact.objects.all()
    return render(request, 'contact/admin_panel.html', {
        'contacto': contacto
    })


@staff_member_required
def contact_create(request):
    """
    -----------------------------------------------------------------------
    Vista: Crear contacto (staff)

    Función
        Mostrar formulario y procesar la creación de un nuevo mensaje
        de contacto desde el panel de administración.

    Patrones utilizados
        • Controller
        • Strategy (GET / POST)
        • PRG

    Flujo

        GET
            ↓
        Mostrar formulario vacío

        POST
            ↓
        Validar datos
            ↓
        Guardar mensaje
            ↓
        Mensaje de éxito
            ↓
        Redireccionar al panel de administración
    -----------------------------------------------------------------------
    """
    if request.method == 'POST':
        form = FormContactUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contacto creado correctamente.')
            return redirect('contact:admin_panel')
    else:
        form = FormContactUser()
    return render(request, 'contact/contact_form.html', {'form': form, 'titulo': 'Crear contacto'})


@staff_member_required
def contact_update(request, pk):
    """
    -----------------------------------------------------------------------
    Vista: Editar contacto (staff)

    Función
        Mostrar formulario precargado y procesar la actualización de
        un mensaje de contacto existente.

    Patrones utilizados
        • Controller
        • Strategy (GET / POST)
        • PRG

    Flujo

        GET
            ↓
        Buscar contacto por pk
            ↓
        Precargar formulario con datos existentes

        POST
            ↓
        Buscar contacto por pk
            ↓
        Validar datos
            ↓
        Guardar cambios
            ↓
        Mensaje de éxito
            ↓
        Redireccionar al panel de administración
    -----------------------------------------------------------------------
    """
    contacto = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        form = FormContactUser(request.POST, instance=contacto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Contacto actualizado correctamente.')
            return redirect('contact:admin_panel')
    else:
        form = FormContactUser(instance=contacto)
    return render(request, 'contact/contact_form.html', {'form': form, 'titulo': 'Editar contacto'})


@staff_member_required
def contact_delete(request, pk):
    """
    -----------------------------------------------------------------------
    Vista: Eliminar contacto (staff)

    Función
        Mostrar confirmación y procesar la eliminación de un mensaje
        de contacto.

    Patrones utilizados
        • Controller
        • Strategy (GET / POST)
        • PRG

    Flujo

        GET
            ↓
        Buscar contacto por pk
            ↓
        Mostrar página de confirmación

        POST
            ↓
        Buscar contacto por pk
            ↓
        Eliminar contacto
            ↓
        Mensaje de éxito
            ↓
        Redireccionar al panel de administración
    -----------------------------------------------------------------------
    """
    contacto = get_object_or_404(Contact, pk=pk)
    if request.method == 'POST':
        contacto.delete()
        messages.success(request, 'Contacto eliminado correctamente.')
        return redirect('contact:admin_panel')
    return render(request, 'contact/contacto_confirm_delete.html', {'contacto': contacto})
