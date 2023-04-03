from . import views
from django.urls import path

urlpatterns = [
    path('', views.home),
    path('registrarUsuario/', views.registrarUsuario),
    path('edicionUsuario/<codigo>', views.edicionUsuario),
    path('editarUsuario/', views.editarUsuario),
    path('eliminarUsuario/<codigo>', views.eliminarUsuario),
    
]