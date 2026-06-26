from django.contrib import admin
from .models import Producto


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'precio', 'disponible', 'created_at']
    list_filter = ['disponible', 'created_at']
    search_fields = ['nombre', 'descripcion']
    ordering = ['-created_at']
