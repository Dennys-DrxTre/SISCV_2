from django.urls import path
from django.contrib.auth import views as auth_views

from apps.inicio.views import DashboardView, AccesoDene, \
    Manten_Client, Manten_Pets, Manten_Client_edit, Manten_Pets_edit, empleadosList, EmpleadosDelete, NotificationView

urlpatterns = [
    path('', DashboardView.as_view(), name='inicio'),
    path('login/', auth_views.LoginView.as_view(template_name='inicio/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='inicio/login.html'), name='logout'),
    path('AccesoDenegado/', AccesoDene.as_view(), name='accesodene'),
    path('notificaciones/', NotificationView.as_view(), name='noti'),

    # MANTENIMIENTO
    path('Mantenimiento/Clientes', Manten_Client.as_view(), name='man_client'),
    path('Mantenimiento/Clientes/Modificar/<int:pk>/',
         Manten_Client_edit.as_view(), name='man_client_edit'),
    path('Mantenimiento/Mascotas', Manten_Pets.as_view(), name='man_pets'),
    path('Mantenimiento/Mascotas/Modificar/<int:pk>/',
         Manten_Pets_edit.as_view(), name='man_pets_edit'),
    path('Mantenimiento/empleados/', empleadosList.as_view(), name='list_emp'),
    path('Mantenimiento/empleados/delete/<int:pk>/',
         EmpleadosDelete.as_view(), name="del_emp"),

]
