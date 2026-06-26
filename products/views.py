from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib import messages
from .models import Producto
from .forms import ProductoForm


def catalogue(request):
    query = request.GET.get('q', '')
    productos = Producto.objects.filter(disponible=True)
    if query:
        productos = productos.filter(nombre__icontains=query)
    return render(request, 'products/catalogue.html', {'productos': productos, 'query': query})


def detail(request, pk):
    producto = get_object_or_404(Producto, pk=pk)
    return render(request, 'products/detail.html', {'producto': producto})


@staff_member_required
def admin_panel(request):
    productos = Producto.objects.all()
    return render(request, 'products/admin_panel.html', {'productos': productos})


@staff_member_required
def producto_create(request):
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
    producto = get_object_or_404(Producto, pk=pk)
    if request.method == 'POST':
        producto.delete()
        messages.success(request, 'Producto eliminado correctamente.')
        return redirect('products:admin_panel')
    return render(request, 'products/producto_confirm_delete.html', {'producto': producto})
