from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.catalogue, name='catalogue'),
    path('admin/', views.admin_panel, name='admin_panel'),
]
