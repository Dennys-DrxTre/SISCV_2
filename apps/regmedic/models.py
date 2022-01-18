from django.db import models
from datetime import datetime, date, time, timedelta

# Create your models here.

# MODELO CLIENTE
class ModeloBase(models.Model):
    estado = models.BooleanField(default=True)
    estado_notificacion = models.BooleanField(default=True, verbose_name='Estado de Notificación')
    prox_cita = models.DateField(default=date.today, verbose_name='Proxima Visita')
    cont_dias = models.IntegerField(default=3)

    class Meta:
        abstract=True

class Cliente(ModeloBase):
    # Nacionalidad
    nat = "V-"
    juri = "J-"
    ex = "E-"
    tipo_cliente = [(nat, 'V-'), (juri, 'J-'), (ex, 'E-')]

    # Codigo de area Movil
    Digitel1 = "0412"
    Movilnet1 = "0416"
    Movilnet2 = "0426"
    Movistar1 = "0414"
    Movistar2 = "0424"
    cod_movil = [(Digitel1, "0412"), (Movilnet1, "0416"),
                 (Movilnet2, "0426"), (Movistar1, "0414"), (Movistar2, "0424")]

    tipo = models.CharField(max_length=10, choices=tipo_cliente, default=nat)
    cedula = models.CharField(primary_key=True, verbose_name="Número de Cédula", max_length=15)
    nombre = models.CharField(verbose_name="Nombres", max_length=40)
    apellido = models.CharField(verbose_name="Apellidos", max_length=40)
    direccion = models.TextField(verbose_name="Direccion Habitacional")
    co_movil = models.CharField(max_length=20, choices=cod_movil, null=True, blank=True)
    movil = models.CharField(verbose_name="Número de Celular", max_length=11, null=True, blank=True)
    tlf = models.CharField(verbose_name="Número de Telefonico", max_length=11, null=True, blank=True)
    correo = models.EmailField(verbose_name="Correo Electronico", null=True, blank=True)
    ocupacion = models.CharField('Ocupación Laboral', max_length=100, null=True, blank=True)
    updated = models.DateField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name_plural = "Clientes"
        ordering = ['-pk']

    def __str__(self):
        return (self.cedula)

# MODELO MASCOTA


class Mascota(ModeloBase):
    nombre = models.CharField(max_length=100, verbose_name='Nombre')
    fnaci = models.DateField(verbose_name='Fecha de Nacimiento')
    sexom = models.CharField(verbose_name='sexo', max_length=40)
    razam = models.CharField(verbose_name='raza', max_length=50)
    peso = models.IntegerField(verbose_name='Peso')
    especie = models.CharField(max_length=50, verbose_name='especie')
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    updated = models.DateField(auto_now=True, verbose_name="Fecha de edición")

    class Meta:
        verbose_name_plural = 'Mascotas'
        ordering = ['-id']

    def __str__(self):
        return self.nombre

# MODELO CONSULTA


class Consulta(ModeloBase):
    motivo = models.TextField(verbose_name='Motivo de Consulta')
    sintomas = models.TextField(verbose_name='Sintomas Presentados', null=True, blank=True)
    diapre = models.TextField(verbose_name='Diagnostico Presuntivo', null=True, blank=True)
    diadef = models.TextField(verbose_name='Diagnostico Definitivo', null=True, blank=True)
    temp = models.TextField(verbose_name='Temperatura', null=True, blank=True)
    frecar = models.TextField(verbose_name='Frecuencia Cardiaca', null=True, blank=True)
    freres = models.TextField(verbose_name='Frecuencia Respiratoria', null=True, blank=True)
    examen = models.TextField(verbose_name='Examenes Realizados', null=True, blank=True)
    trata = models.TextField(verbose_name='Tratamientos Aplicados', null=True, blank=True)
    fechac = models.DateTimeField(verbose_name='Fecha de Creacion', auto_now_add=True)
    fechaa = models.DateTimeField(verbose_name='Fecha de Actualizacion', auto_now=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Consultas'
        ordering = ['-fechac']

    def __str__(self):
        return self.motivo

# MODELO DESPARASITACION

class Despa(ModeloBase):
    despa = models.TextField(verbose_name='Desparasitante', null=True, blank=True)
    descripcion = models.TextField(verbose_name='Descripcion', default="", null=True, blank=True)
    fechad = models.DateTimeField(verbose_name='Fecha de Actualizacion', auto_now=True)
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Desparasitaciones'
        ordering = ['fechad']

    def __str__(self):
        return self.despa

# MODELO VACUNA

class Vacuna(ModeloBase):
    nomva = models.TextField(verbose_name='Nombre de la Vacuna/s')
    fechav = models.DateField(verbose_name='Fecha de Actualizacion', auto_now=True)
    dosis = models.TextField(verbose_name='Dosis')
    mascota = models.ForeignKey(Mascota, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Vacunaciones'
        ordering = ['fechav']

    def __str__(self):
        return self.nomva
