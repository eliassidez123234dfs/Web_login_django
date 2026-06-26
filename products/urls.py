from django.urls import path
from . import views

app_name = 'products'

urlpatterns = [
    path('', views.catalogue, name='catalogue'),
    path('<int:pk>/', views.detail, name='detail'),
    path('admin/', views.admin_panel, name='admin_panel'),
]
