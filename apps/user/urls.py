from django.urls import path

from . import views

urlpatterns = [
    path('usuarios/', views.ListUser.as_view(), name='usuarios'),
    path('usuarios2/', views.listado_users, name='usuarios2'),
]
