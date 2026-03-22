from django.urls import path
from . import views

urlpatterns = [
    path('', views.device_list, name='device_list'),
    path('add/', views.add_device, name='add_device'),
    path('lookup/', views.ip_lookup, name='ip_lookup'),
    path('edit/<int:id>/', views.edit_device, name='edit_device'),
    path('delete/<int:id>/', views.delete_device, name='delete_device'),
]