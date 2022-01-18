import threading
from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required, permission_required
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.core import serializers
from django.forms import model_to_dict
from datetime import datetime, date, timedelta

from apps.regmedic.models import Cliente, Mascota, Consulta, Despa, Vacuna
from apps.regmedic .forms import ClienteForm, MascotaForm

from django.db.models import Count
from django.utils.timezone import datetime
from notifications.signals import notify


def send_notify_push(user_username, user_id):
    try:
        date_today = date.today()
        # Consulta
        for c in Consulta.objects.filter(estado_notificacion = True):
            c.prox_cita = c.prox_cita - timedelta(days=1)
            if c.prox_cita == date_today:
                sender = User.objects.get(username=user_username)
                receiver = User.objects.get(id=user_id)
                c.estado_notificacion = False
                c.prox_cita = c.prox_cita + timedelta(days=1)
                notify.send(sender, recipient=receiver, verb=f'Consulta pendiente para {c.prox_cita.strftime("%d/%m/%Y")}', description=f'cliente: {c.mascota.cliente.cedula}, contacto: {c.mascota.cliente.co_movil}-{c.mascota.cliente.movil}, su mascota: {c.mascota.nombre}', level='success') 
                c.save()
            else:
                continue

        # Vacunación
        for d in Despa.objects.filter(estado_notificacion = True):
            d.prox_cita = d.prox_cita - timedelta(days=1)
            if d.prox_cita == date_today:
                sender = User.objects.get(username=user_username)
                receiver = User.objects.get(id=user_id)
                d.estado_notificacion = False
                d.prox_cita = d.prox_cita + timedelta(days=1)
                notify.send(sender, recipient=receiver, verb=f'Desparasitación pendiente para {d.prox_cita.strftime("%d/%m/%Y")}', description=f'cliente: {d.mascota.cliente.cedula}, contacto: {d.mascota.cliente.co_movil}-{d.mascota.cliente.movil}, su mascota: {d.mascota.nombre}', level='error') 
                d.save()
            else:
                continue

        # Vacunación
        for v in Vacuna.objects.filter(estado_notificacion = True):
            v.prox_cita = v.prox_cita - timedelta(days=1)
            if v.prox_cita == date_today:
                sender = User.objects.get(username=user_username)
                receiver = User.objects.get(id=user_id)
                v.estado_notificacion = False
                v.prox_cita = v.prox_cita + timedelta(days=1)
                notify.send(sender, recipient=receiver, verb=f'Vacunación pendiente para {v.prox_cita.strftime("%d/%m/%Y")}', description=f'cliente: {v.mascota.cliente.cedula}, contacto: {v.mascota.cliente.co_movil}-{v.mascota.cliente.movil}, su mascota: {v.mascota.nombre}', level='info') 
                v.save()
            else:
                continue
   
    except Exception as e:
        print(e)

# Create your views here.
class SinPermiso(PermissionRequiredMixin, LoginRequiredMixin):
    login_url = 'inicio:login'
    raise_exception = False
    redirect_field_name = "redirect_to"

    def handle_no_permission(self):
        from django.contrib.auth.models import AnonymousUser
        if not self.request.user == AnonymousUser():
            self.login_url = 'inicio:accesodene'
        return HttpResponseRedirect(reverse_lazy(self.login_url))


class FechaHora():
    Hoy = datetime.today()

class DashboardView(LoginRequiredMixin, TemplateView):
    template_name = 'inicio/inicio.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get (self, request,*args, **kwargs):
        date_today = date.today()

        consulta_hoy = Consulta.objects.filter(prox_cita=date_today)
        vacunacion_hoy = Vacuna.objects.filter(prox_cita=date_today)
        despa_hoy = Despa.objects.filter(prox_cita=date_today)

        # Los 5 ultimos movimientos
        clientes = Cliente.objects.all().order_by('-updated')
        mascotas = Mascota.objects.all().order_by('-id')
        consult = Consulta.objects.all().order_by('-id')

        thread = threading.Thread(target=send_notify_push(request.user.username, request.user.id))
        thread.start()

        context = {
            'cliente': clientes,
            'mascota': mascotas,
            'consulta': consult,
            'date_today': date_today.strftime('%d/%m/%Y'),
            'consulta_hoy': consulta_hoy,
            'vacunacion_hoy': vacunacion_hoy,
            'despa_hoy': despa_hoy,
        }

        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'read':
                obj = request.user.notifications.get(id=request.POST['id'])
                obj.unread = False
                obj.save()
            else:
                data['error'] = 'Ha ocurrido un error'
                
        except Exception as e:
            data['error'] = str(e)
            print(data)
        return JsonResponse(data, safe=False)

class AccesoDene(LoginRequiredMixin, generic.TemplateView):
    template_name = 'inicio/sin_privilegios.html'
    login_url = 'inicio:login'

# VIEWS DE MANTENIMIENTO
# CLIENTES
class Manten_Client(SinPermiso, generic.ListView):
    model = Cliente
    template_name = "inicio/Manten_Cliente.html"
    permission_required = "admin.view_entry"


class Manten_Client_edit(SinPermiso, generic.UpdateView):
    model = Cliente
    context_object_name = "obj"
    form_class = ClienteForm
    template_name = "inicio/Manten_Cliente_Edit.html"
    success_url = reverse_lazy('inicio:man_client')
    permission_required = "admin.edit_entry"

# MASCOTAS

class Manten_Pets(SinPermiso, generic.ListView):
    model = Mascota
    template_name = "inicio/Manten_Pets.html"
    permission_required = "admin.view_entry"


class Manten_Pets_edit(SinPermiso, generic.UpdateView):
    template_name = "inicio/Manten_Pets_Edit.html"
    model = Mascota
    context_object_name = "obj"
    form_class = MascotaForm
    success_url = reverse_lazy('inicio:man_pets')
    permission_required = "admin.edit_entry"

# EMPLEADOS
class empleadosList(SinPermiso, generic.ListView):
    model = User
    template_name = "inicio/NuevoEmpleado.html"
    permission_required = "admin.view_entry"

class EmpleadosDelete(SinPermiso, generic.DeleteView):
    model = User
    template_name = "inicio/DeleteEmpleado.html"
    success_url = reverse_lazy('inicio:list_emp')
    context_object_name = "obj"
    permission_required = "admin.delete_entry"


class NotificationView(LoginRequiredMixin, TemplateView):
    template_name = 'inicio/email_inbox_card.html'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']

            if action == 'search_all':
                data = list(request.user.notifications.all().values('id', 'level', 'unread', 'verb', 'description','timestamp'))
                for i in data:
                    i['timestamp'] = i['timestamp'].date().strftime('%d/%m/%Y')
                    if i['unread']:
                        i['unread'] = 'No leido'
                    else:
                        i['unread'] = 'Leido'
                    
                    if i['level'] == 'success':
                        i['level'] = 'CONSULTA'
                    elif i['level'] == 'info':
                        i['level'] = 'VACUNACIÓN'
                    elif i['level'] == 'error':
                        i['level'] = 'DESPARASITACIÓN'  

            elif action == 'all_read':
                request.user.notifications.mark_all_as_read()

            elif action == 'one_read':
                obj = request.user.notifications.get(id=request.POST['id'])
                obj.unread = False
                obj.save()

            elif action == 'one_delete':
                obj = request.user.notifications.get(id=request.POST['id'])
                obj.delete()

            elif action == 'all_delete':
                for obj in request.user.notifications.all():
                    obj.delete()
        
            else:
                data['error'] = 'Ha ocurrido un error'
                
        except Exception as e:
            data['error'] = str(e)
            print(data)
        return JsonResponse(data, safe=False)