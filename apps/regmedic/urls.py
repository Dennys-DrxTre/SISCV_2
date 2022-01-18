from django.urls import path

from .views import ClienteView, ClienteNuevo, ClienteEdit, ClienteInact, ClienteDetail, MascotaView, MascotaNew, MascotaDetail, MascotaEdit, MascotaInact, ConsultaView, ConsultaNew, ConsultaEdit, ConsultaDel, ConsultaDetail, VacunaView, VacunaNew, VacunaEdit, VacunaDel, DespaView, DespaNew, DespaEdit, DespaDel, ClienteDelete, Mascota_Delete

urlpatterns = [
#URLS CLIENTES
    path('Clientes', ClienteView.as_view(), name='Cliente_list'),
    path('Cliente/new', ClienteNuevo.as_view(), name='Cliente_form'),
    path('Cliente/edit/<int:pk>', ClienteEdit.as_view(), name='Cliente_edit'),
    path('Cliente/inac/<int:id>', ClienteInact, name='Cliente_inac'),
    path('Cliente/detail/<int:pk>', ClienteDetail.as_view(), name='Cliente_detail'),
    path('Cliente/<int:pk>/delete', ClienteDelete.as_view(), name='Cliente_delete'),
#URLS MASCOTAS
    path('Mascotas', MascotaView.as_view(), name='Mascota_list'),
    path('Mascota/new', MascotaNew.as_view(), name='Mascota_form'),
    path('Mascota/detail/<int:pk>', MascotaDetail.as_view(), name='Mascota_detail'),
    path('Mascota/edit/<int:pk>', MascotaEdit.as_view(), name='Mascota_edit'),
    path('Mascota/inac/<int:id>', MascotaInact, name='Mascota_inac'),
    path('Mascota/<int:pk>/delete/', Mascota_Delete.as_view(), name='Mascota_delete'),
#URLS CONSULTAS
    path('Consultas', ConsultaView.as_view(), name='Consulta_list'),
    path('Consulta/new', ConsultaNew.as_view(), name='Consulta_form'),
    path('Consulta/edit/<int:pk>', ConsultaEdit.as_view(), name='Consulta_edit'),
    path('Consulta/eliminar/<int:pk>', ConsultaDel.as_view(), name='Consulta_del'),
    path('Consulta/detail/<int:pk>', ConsultaDetail.as_view(), name='Consulta_detail'),
#URLS VACUNACIONES
    path('Vacunas', VacunaView.as_view(), name='Vacuna_list'),
    path('Vacuna/new', VacunaNew.as_view(), name='Vacuna_form'),
    path('Vacuna/edit/<int:pk>', VacunaEdit.as_view(), name='Vacuna_edit'),
    path('Vacuna/eliminar/<int:pk>', VacunaDel.as_view(), name='Vacuna_del'),
#URLS DESPARASITACIONES
    path('Despa', DespaView.as_view(), name='Despa_list'),
    path('Despa/new', DespaNew.as_view(), name='Despa_form'),
    path('Despa/edit/<int:pk>', DespaEdit.as_view(), name='Despa_edit'),
    path('Despa/eliminar/<int:pk>', DespaDel.as_view(), name='Despa_del'),

]
