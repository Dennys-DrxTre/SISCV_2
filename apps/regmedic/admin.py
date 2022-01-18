from django.contrib import admin
from .models import Mascota, Cliente, Consulta, Despa, Vacuna 
# Register your models here.

admin.site.register(Mascota)
admin.site.register(Cliente)
admin.site.register(Consulta)
admin.site.register(Despa)
admin.site.register(Vacuna)