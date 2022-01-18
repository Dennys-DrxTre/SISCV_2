from django.shortcuts import render, redirect, HttpResponse, HttpResponseRedirect
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required


from apps.inicio.views import SinPermiso
from .models import Cliente, Mascota, Consulta, Vacuna, Despa
from .forms import ClienteForm, MascotaForm, ConsultaForm, VacunaForm, DespaForm

# Create your views here.

# VISTAS CLIENTES


class ClienteView(SinPermiso, generic.ListView):
    model = Cliente
    template_name = 'regmedic/Cliente_list.html'
    context_object_name = 'obj'
    permission_required = "regmedic.view_cliente"


class ClienteNuevo(SuccessMessageMixin, SinPermiso, generic.CreateView):
    model = Cliente
    template_name = 'regmedic/Cliente_form.html'
    context_object_name = "obj"
    form_class = ClienteForm
    success_url = reverse_lazy('regmedic:Cliente_list')
    success_message = 'Cliente Agregado Correctamente'
    permission_required = "regmedic.add_cliente"


class ClienteEdit(SuccessMessageMixin, SinPermiso, generic.UpdateView):
    model = Cliente
    template_name = 'regmedic/Cliente_edit_form.html'
    context_object_name = "obj"
    form_class = ClienteForm
    success_url = reverse_lazy('regmedic:Cliente_list')
    success_message = 'Cliente Actualizado Correctamente'
    permission_required = "regmedic.change_cliente"


@login_required(login_url='/login/')
@permission_required('regmedic.change_cliente', login_url='inicio:accesodene')
def ClienteInact(request, id):
    cliente = Cliente.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'regmedic/Cliente_del.html'

    if not cliente:
        return redirect('regmedic:Cliente_list')

    if request.method == 'GET':
        contexto = {'obj': cliente}

    if request.method == 'POST':
        if cliente.estado == True:
            cliente.estado = False
            cliente.save()
            messages.success(request, 'Cliente Desactivado Correctamente')

        else:
            cliente.estado = True
            cliente.save()
            messages.success(request, 'Cliente Activado Correctamente')
        return redirect('regmedic:Cliente_list')

    return render(request, template_name, contexto)


class ClienteDetail(SinPermiso, generic.DetailView):
    permission_required = "regmedic.view_cliente"

    def get(self, request, pk, *args, **kwargs):
        cliente = Cliente.objects.get(pk=pk)
        Mascotas = Mascota.objects.filter(cliente=pk)
        return render(request, "regmedic/Cliente_detail.html", {'obj': cliente, 'objm': Mascotas})


class ClienteDelete(SinPermiso, generic.DeleteView):
    model = Cliente
    template_name = "regmedic/Cliente_delete.html"
    success_url = reverse_lazy('inicio:man_client')
    success_message = "Cliente Eliminado Correctamente"
    context_object_name = "obj"
    permission_required = "regmedic.delete_cliente"

# VISTAS MASCOTAS


class MascotaView(LoginRequiredMixin, generic.ListView):
    model = Mascota
    template_name = 'regmedic/Mascota_list.html'
    context_object_name = 'obj'
    permission_required = "regmedic.view_mascota"


class MascotaNew(SuccessMessageMixin, SinPermiso, generic.CreateView):
    model = Mascota
    template_name = 'regmedic/Mascota_form.html'
    context_object_name = "obj"
    form_class = MascotaForm
    success_url = reverse_lazy('regmedic:Mascota_list')
    success_message = 'Mascota Agregada Correctamente'
    permission_required = "regmedic.add_mascota"


class MascotaDetail(SinPermiso, generic.DetailView):
    permission_required = "regmedic.view_mascota"

    def get(self, request, pk, *args, **kwargs):
        mascota = Mascota.objects.get(pk=pk)
        consulta = Consulta.objects.filter(mascota=pk)
        vacun = Vacuna.objects.filter(mascota=pk)
        desp = Despa.objects.filter(mascota=pk)
        return render(request, 'regmedic/Mascota_detail.html', {'obj': mascota, 'objc': consulta, 'objv': vacun, 'objd': desp})


class MascotaEdit(SuccessMessageMixin, SinPermiso, generic.UpdateView):
    model = Mascota
    template_name = 'regmedic/Mascota_edit_form.html'
    context_object_name = "obj"
    form_class = MascotaForm
    success_url = reverse_lazy('regmedic:Mascota_list')
    success_message = 'Mascota Actualizada Correctamente'
    permission_required = "regmedic.change_mascota"


@login_required(login_url='/login/')
@permission_required('regmedic.change_mascota', login_url='inicio:accesodene')
def MascotaInact(request, id):
    mascota = Mascota.objects.filter(pk=id).first()
    contexto = {}
    template_name = 'regmedic/Mascota_del.html'

    if not mascota:
        return redirect('regmedic:Mascota_list')

    if request.method == 'GET':
        contexto = {'obj': mascota}

    if request.method == 'POST':
        if mascota.estado == True:
            mascota.estado = False
            mascota.save()
            messages.success(request, 'Mascota Activada Correctamente')

        else:
            mascota.estado = True
            mascota.save()
            messages.success(request, 'Mascota Desactivada Correctamente')

        return redirect('regmedic:Mascota_list')

    return render(request, template_name, contexto)


class Mascota_Delete(SinPermiso, generic.DeleteView):
    model = Mascota
    template_name = "regmedic/Mascota_delete.html"
    success_url = reverse_lazy('inicio:man_pets')
    success_message = "Mascota Eliminada Correctamente"
    context_object_name = "obj"
    permission_required = "regmedic.delete_mascota"

# VISTAS CONSULTAS


class ConsultaView(SinPermiso, generic.ListView):
    model = Consulta
    template_name = 'regmedic/Consulta_list.html'
    context_object_name = 'obj'
    permission_required = "regmedic.view_consulta"


class ConsultaNew(SuccessMessageMixin, SinPermiso, generic.CreateView):
    model = Consulta
    template_name = 'regmedic/Consulta_form.html'
    context_object_name = "obj"
    form_class = ConsultaForm
    success_url = reverse_lazy('regmedic:Consulta_list')
    success_message = 'Consulta Agregada Correctamente'
    permission_required = "regmedic.add_consulta"


class ConsultaEdit(SuccessMessageMixin, SinPermiso, generic.UpdateView):
    model = Consulta
    template_name = 'regmedic/Consulta_edit_form.html'
    context_object_name = "obj"
    form_class = ConsultaForm
    success_url = reverse_lazy('regmedic:Consulta_list')
    success_message = 'Consulta Actualizada Correctamente'
    permission_required = "regmedic.change_consulta"


class ConsultaDel(SuccessMessageMixin, SinPermiso, generic.DeleteView):
    model = Consulta
    template_name = 'regmedic/Consulta_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('regmedic:Consulta_list')
    success_message = 'Consulta Eliminada Correctamente'
    permission_required = "regmedic.delete_consulta"


class ConsultaDetail(SinPermiso, generic.DetailView):
    permission_required = "regmedic.view_consulta"
    model = Consulta
    template_name = 'regmedic/Consulta_detail.html'
    context_object_name = 'consulta'

# VISTAS VACUNACION


class VacunaView(SinPermiso, generic.ListView):
    model = Vacuna
    template_name = 'regmedic/Vacuna_list.html'
    context_object_name = 'obj'
    permission_required = "regmedic.view_vacuna"


class VacunaNew(SuccessMessageMixin, SinPermiso, generic.CreateView):
    model = Vacuna
    template_name = 'regmedic/Vacuna_form.html'
    context_object_name = "obj"
    form_class = VacunaForm
    success_url = reverse_lazy('regmedic:Vacuna_list')
    success_message = 'Vacunación Agregada Correctamente'
    permission_required = "regmedic.add_vacuna"


class VacunaEdit(SuccessMessageMixin, SinPermiso, generic.UpdateView):
    model = Vacuna
    template_name = 'regmedic/Vacuna_edit.html'
    context_object_name = "obj"
    form_class = VacunaForm
    success_url = reverse_lazy('regmedic:Vacuna_list')
    success_message = 'Vacunación Actualizada Correctamente'
    permission_required = "regmedic.change_vacuna"


class VacunaDel(SuccessMessageMixin, SinPermiso, generic.DeleteView):
    model = Vacuna
    template_name = 'regmedic/Vacuna_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('regmedic:Vacuna_list')
    success_message = 'Vacunación Eliminada Correctamente'
    permission_required = "regmedic.delete_vacuna"


# VISTAS DESPARASITACIóN

class DespaView(SinPermiso, generic.ListView):
    model = Despa
    template_name = 'regmedic/Despa_list.html'
    context_object_name = 'obj'
    permission_required = "regmedic.view_despa"


class DespaNew(SuccessMessageMixin, SinPermiso, generic.CreateView):
    model = Despa
    template_name = 'regmedic/Despa_form.html'
    context_object_name = "obj"
    form_class = DespaForm
    success_url = reverse_lazy('regmedic:Despa_list')
    success_message = 'Desparasitación Agregada Correctamente'
    permission_required = "regmedic.add_despa"


class DespaEdit(SuccessMessageMixin, SinPermiso, generic.UpdateView):
    model = Despa
    template_name = 'regmedic/Despa_edit.html'
    context_object_name = "obj"
    form_class = DespaForm
    success_url = reverse_lazy('regmedic:Despa_list')
    success_message = 'Desparasitación Actualizada Correctamente'
    permission_required = "regmedic.change_despa"


class DespaDel(SuccessMessageMixin, SinPermiso, generic.DeleteView):
    model = Despa
    template_name = 'regmedic/Despa_del.html'
    context_object_name = 'obj'
    success_url = reverse_lazy('regmedic:Despa_list')
    success_message = 'Desparasitación Eliminada Correctamente'
    permission_required = "regmedic.delete_despa"
