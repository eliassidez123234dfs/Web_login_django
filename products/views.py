"""
===========================================================================
MÓDULO DE VISTAS (products/views.py)
===========================================================================

Este archivo implementa la lógica de negocio del módulo de productos.

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
===========================================================================
"""

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm


def catalogue(request):
    """
    -----------------------------------------------------------------------
    Vista: Catálogo de productos

    Función
        Mostrar el catálogo público de productos disponibles.
        Permite filtrar por nombre mediante el parámetro de búsqueda 'q'.

    Patrones utilizados
        • Controller
        • MVT

    Flujo

        Usuario
            ↓
        Solicita catálogo (con o sin query)
            ↓
        Filtra productos disponibles y por nombre si hay query
            ↓
        Renderiza catalogue.html con productos y query
    -----------------------------------------------------------------------
    """
    query = request.GET.get('q', '')
    productos = Producto.objects.filter(disponible=True)
    if query:
        productos = productos.filter(nombre__icontains=query)
    return render(request, 'products/catalogue.html', {'productos': productos, 'query': query})


def detail(request, pk):
    """
    -----------------------------------------------------------------------
    Vista: Detalle de producto

    Función
        Mostrar la información detallada de un producto específico.

    Patrones utilizados
        • Controller
        • MVT

    Flujo

        Usuario
            ↓
        Solicita detalle con pk
            ↓
        Busca producto por pk (404 si no existe)
            ↓
        Renderiza detail.html con producto
    -----------------------------------------------------------------------
    """
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'products/detail.html', {'producto': producto})


@staff_member_required
def admin_panel(request):
    """
    -----------------------------------------------------------------------
    Vista: Panel de administración de productos

    Función
        Listar todos los productos (incluyendo no disponibles) para
        su gestión por parte del staff.

    Patrones utilizados
        • Controller
        • MVT
        • Restricción de acceso

    Flujo

        Staff
            ↓
        Solicita panel de administración
            ↓
        Obtiene todos los productos
            ↓
        Renderiza admin_panel.html con productos
    -----------------------------------------------------------------------
    """
    productos = Producto.objects.all()
    return render(request, 'products/admin_panel.html', {'productos': productos})


@staff_member_required
def producto_create(request):
    """
    -----------------------------------------------------------------------
    Vista: Crear producto

    Función
        Mostrar formulario y procesar la creación de un nuevo producto
        con imagen opcional.

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
        Validar datos (incluyendo archivos)
            ↓
        Guardar producto
            ↓
        Mensaje de éxito
            ↓
        Redireccionar al panel de administración
    -----------------------------------------------------------------------
    """
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto creado correctamente.')
            return redirect('products:admin_panel')
    else:
        form = ProductoForm()
    return render(request, 'products/producto_form.html', {'form': form, 'titulo': 'Crear producto'})


@staff_member_required
def producto_update(request, pk):
    """
    -----------------------------------------------------------------------
    Vista: Editar producto

    Función
        Mostrar formulario precargado y procesar la actualización de
        un producto existente.

    Patrones utilizados
        • Controller
        • Strategy (GET / POST)
        • PRG

    Flujo

        GET
            ↓
        Buscar producto por pk
            ↓
        Precargar formulario con datos existentes

        POST
            ↓
        Buscar producto por pk
            ↓
        Validar datos (incluyendo archivos)
            ↓
        Guardar cambios
            ↓
        Mensaje de éxito
            ↓
        Redireccionar al panel de administración
    -----------------------------------------------------------------------
    """
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        form = ProductoForm(request.POST, request.FILES, instance=producto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Producto actualizado correctamente.')
            return redirect('products:admin_panel')
    else:
        form = ProductoForm(instance=producto)
    return render(request, 'products/producto_form.html', {'form': form, 'titulo': 'Editar producto'})


@staff_member_required
def producto_delete(request, pk):
    """
    -----------------------------------------------------------------------
    Vista: Eliminar producto

    Función
        Mostrar confirmación y procesar la eliminación de un producto.

    Patrones utilizados
        • Controller
        • Strategy (GET / POST)
        • PRG

    Flujo

        GET
            ↓
        Buscar producto por pk
            ↓
        Mostrar página de confirmación

        POST
            ↓
        Buscar producto por pk
            ↓
        Eliminar producto
            ↓
        Mensaje de éxito
            ↓
        Redireccionar al panel de administración
    -----------------------------------------------------------------------
    """
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return redirect('products:admin_panel')
    return render(request, 'products/producto_confirm_delete.html', {'producto': producto})
