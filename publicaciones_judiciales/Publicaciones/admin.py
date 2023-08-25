from django.contrib import admin
from .models import Remate, Licitacion, Martillero, Cliente, Operador

# Register your models here.

admin.site.register(Remate)
admin.site.register(Licitacion)
admin.site.register(Martillero)
admin.site.register(Cliente)
admin.site.register(Operador)