import os
from django.conf import settings
from django.http import HttpResponse
from django.template.loader import get_template
from xhtml2pdf import pisa
from django.utils import timezone

from apps.regmedic.models import Cliente, Mascota, Consulta, Vacuna, Despa


def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    # use short variable names
    sUrl = settings.STATIC_URL      # Typically /static/
    sRoot = settings.STATIC_ROOT    # Typically /home/userX/project_static/
    mUrl = settings.MEDIA_URL       # Typically /static/media/
    mRoot = settings.MEDIA_ROOT     # Typically /home/userX/project_static/media/

    # convert URIs to absolute system paths
    if uri.startswith(mUrl):
        path = os.path.join(mRoot, uri.replace(mUrl, "/media/"))
    elif uri.startswith(sUrl):
        path = os.path.join(sRoot, uri.replace(sUrl, ""))
    else:
        return uri  # handle absolute uri (ie: http://some.tld/foo.png)

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception(
            'media URI must start with %s or %s' % (sUrl, mUrl)
        )
    return path

# CLIENTES


def reportcliente_all(request):
    template_path = 'reporte/report_cliente_all.html'
    today = timezone.now()

    cliente = Cliente.objects.filter(estado=True)
    context = {
        'obj': cliente,
        'today': today,
        'request': request
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="Todas los Clientes.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

# MASCOTA


def reportmascota_all(request):
    template_path = 'reporte/report_mascota_all.html'
    today = timezone.now()

    mascota = Mascota.objects.filter(estado=True)
    context = {
        'obj': mascota,
        'today': today,
        'request': request
    }

    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="Todas las macotas.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def reportclient_one(request, cedula):
    template_path = 'reporte/report_cliente_one.html'
    today = timezone.now

    cliente = Cliente.objects.filter(pk=cedula).first()
    mascota = Mascota.objects.filter(cliente=cedula)
    context = {
        'obj': cliente,
        'mascota': mascota,
        'today': today,
        'request': request
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="Detalle del cliente.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def reportmascot_one(request, id):
    template_path = 'reporte/report_mascota_one.html'
    today = timezone.now

    mascota = Mascota.objects.filter(pk=id).first()
    consulta = Consulta.objects.filter(mascota=id)
    desparasitacion = Despa.objects.filter(mascota=id)
    vacunacion = Vacuna.objects.filter(mascota=id)

    context = {
        'mascota': mascota,
        'consulta': consulta,
        'vacuna': vacunacion,
        'despa': desparasitacion,
        'today': today,
        'request': request
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="Detalle de la mascota.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response


def reportConsulta(request, id):
    template_path = 'reporte/report_consulta.html'
    today = timezone.now

    consulta = Consulta.objects.filter(pk=id).first()
    mas = Mascota.objects.filter(pk=consulta.id).first()

    context = {
        'mascota': mas,
        'consulta': consulta,
        'today': today,
        'request': request
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="Detalle de la consulta.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def reportDespa(request, id):
    template_path = 'reporte/report_desparasitacion.html'
    today = timezone.now

    despa = Despa.objects.filter(pk=id).first()
    mas = Mascota.objects.filter(pk=despa.id).first()

    context = {
        'mascota': mas,
        'despa': despa,
        'today': today,
        'request': request
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="Detalle de la desparasitacion.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response

def reportVacuna(request, id):
    template_path = 'reporte/report_vacuna.html'
    today = timezone.now

    vac = Vacuna.objects.filter(pk=id).first()
    mas = Mascota.objects.filter(pk=vac.id).first()

    context = {
        'mascota': mas,
        'vacuna': vac,
        'today': today,
        'request': request
    }
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'inline; filename="Detalle de la vacunacion.pdf"'
    template = get_template(template_path)
    html = template.render(context)

    pisaStatus = pisa.CreatePDF(
        html, dest=response, link_callback=link_callback)
    if pisaStatus.err:
        return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response
