from django.urls import path
from .views import *

urlpatterns = [
    path('remates/', remates, name='remates'),
    path('busqueda_remates/', busquedaRemate, name='busqueda_remates'),
    path('remates_encontrados/', busquedaBien, name='buscar_rema'),
    path('eliminar_remate/<id>', eliminar_remate, name='eliminar_remate'),
    path('editar_remate/<id>', editar_remate, name='editar_remate'),
    path('licitaciones/', licitaciones, name='licitaciones'),
    path('busqueda_licitaciones/', busquedaLicitacion, name='busqueda_licitaciones'),
    path('licitaciones_encontradas/', busquedaObjeto, name='buscar_lici'),
    path('martilleros/', martilleros, name='martilleros'),
    path('clientes/', clientes, name='clientes'),
    path('operadores/', operadores, name='operadores'),
]