from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.catalogue, name='catalogue'),
    path('<int:pk>/', views.detail, name='detail'),
    path('admin/', views.admin_panel, name='admin_panel'),
    path('admin/crear/', views.producto_create, name='producto_create'),
    path('admin/<int:pk>/editar/', views.producto_update, name='producto_update'),
    path('admin/<int:pk>/eliminar/', views.producto_delete, name='producto_delete'),
]
