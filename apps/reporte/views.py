from django.conf import settings
from io import BytesIO
from reportlab.pdfgen import canvas
from django.views.generic import View
from django.http import HttpResponse
from reportlab.platypus import SimpleDocTemplate, Paragraph, TableStyle
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib import colors
from reportlab.lib.pagesizes import letter
from reportlab.platypus import Table
from django.utils import timezone, dates

from apps.regmedic.models import Cliente

class ReportePersonasPDF(View):  
    
    def cabecera(self,pdf):
        #Utilizamos el archivo logo_django.png que está guardado en la carpeta media/imagenes
        archivo_imagen = settings.MEDIA_ROOT+'/logo1.png'
        #Definimos el tamaño de la imagen a cargar y las coordenadas correspondientes
        pdf.drawImage(archivo_imagen, 40, 770, 80, 40,preserveAspectRatio=True)
        #Dibujamos una cadena en la ubicación X,Y especificada
        pdf.setFont("Helvetica", 14)
        pdf.drawString(200, 750, u"LISTADO DE CLIENTES")
        
        pdf.setFont("Helvetica", 10)
        today = timezone.datetime.now()
        pdf.drawString(450, 750, 'Fecha: '+str(today.day)+'/'+str(today.month)+'/'+str(today.year))
              

    def get(self, request, *args, **kwargs):
            #Indicamos el tipo de contenido a devolver, en este caso un pdf
            response = HttpResponse(content_type='application/pdf')
            response['Content-Disposition'] = 'inline; filename="Listado de Clientes.pdf "' 

            #La clase io.BytesIO permite tratar un array de bytes como un fichero binario, se utiliza como almacenamiento temporal
            buffer = BytesIO()
            #Canvas nos permite hacer el reporte con coordenadas X y Y
            pdf = canvas.Canvas(buffer)
            #Llamo al método cabecera donde están definidos los datos que aparecen en la cabecera del reporte.
            self.cabecera(pdf)
            y = 600
            self.tabla(pdf, y)
            #Con show page hacemos un corte de página para pasar a la siguiente
            pdf.setTitle('Clientes')
            pdf.showPage()
            pdf.save()
            pdf = buffer.getvalue()
            buffer.close()
            response.write(pdf)
            return response

    def tabla(self,pdf,y):
        #Creamos una tupla de encabezados para neustra tabla
        encabezados = (
            'Cedula',
            'Nombre Apellido',
            'Movil',
            'Email', 
            'Dirección'
        )
        #Creamos una lista de tuplas que van a contener a las personas
        detalles =  [( 
            p.tipo+p.cedula,
            p.nombre+' '+p.apellido, 
            p.co_movil+p.movil, 
            p.correo, 
            p.direccion 
        ) for p in Cliente.objects.all().order_by('-updated')]
        #Establecemos el tamaño de cada una de las columnas de la tabla
        detalle_orden = Table([encabezados] + detalles)
        #Aplicamos estilos a las celdas de la tabla
        detalle_orden.setStyle(TableStyle(
            [
                #La primera fila(encabezados) va a estar centrada
                ('ALIGN',(0,0),(4,0),'CENTER'),
                #Los bordes de todas las celdas serán de color negro y con un grosor de 1
                ('GRID', (0, 0), (-1, -1), 1, colors.black), 
                #El tamaño de las letras de cada una de las celdas será de 9
                ('FONTSIZE', (0, 0), (-1, -1), 9),
            ]
        ))
        #Establecemos el tamaño de la hoja que ocupará la tabla 
        detalle_orden.wrapOn(pdf, 800, 600)
        #Definimos la coordenada donde se dibujará la tabla
        detalle_orden.drawOn(pdf, 70,560)

