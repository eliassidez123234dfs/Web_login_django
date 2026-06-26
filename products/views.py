from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from .models import Producto


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
    return render(request, 'products/admin_panel.html')
