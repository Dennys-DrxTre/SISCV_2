from django.urls import path, re_path
from .reportes import reportmascota_all,\
    reportclient_one, reportmascot_one, reportcliente_all, reportConsulta, reportDespa, reportVacuna
from .views import ReportePersonasPDF


urlpatterns = [
    path('mascotaall/', reportmascota_all, name='mascotaall'),
    path('cliente/one/<int:cedula>', reportclient_one, name='clienteone'),
    path('mascota/one/<int:id>', reportmascot_one, name='mascotaone'),
    path('consulta/<int:id>', reportConsulta, name='consultaDet'),
    path('desparasitacion/<int:id>', reportDespa, name='despaPdf'),
    path('vacunacion/<int:id>', reportVacuna, name='vacunaPdf'),
    path('clienteall/', reportcliente_all, name='clientall'),
    path('allclient/', ReportePersonasPDF.as_view(), name='reportclient')
]
