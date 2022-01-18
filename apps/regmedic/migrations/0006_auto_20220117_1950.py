# Generated by Django 3.0.7 on 2022-01-18 00:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('regmedic', '0005_auto_20220114_1303'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='estado_notificacion',
            field=models.BooleanField(default=True, verbose_name='Estado de Notificación'),
        ),
        migrations.AlterField(
            model_name='cliente',
            name='prox_cita',
            field=models.DateField(default=datetime.date.today, verbose_name='Proxima Visita'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='estado_notificacion',
            field=models.BooleanField(default=True, verbose_name='Estado de Notificación'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='prox_cita',
            field=models.DateField(default=datetime.date.today, verbose_name='Proxima Visita'),
        ),
        migrations.AlterField(
            model_name='despa',
            name='estado_notificacion',
            field=models.BooleanField(default=True, verbose_name='Estado de Notificación'),
        ),
        migrations.AlterField(
            model_name='despa',
            name='prox_cita',
            field=models.DateField(default=datetime.date.today, verbose_name='Proxima Visita'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='estado_notificacion',
            field=models.BooleanField(default=True, verbose_name='Estado de Notificación'),
        ),
        migrations.AlterField(
            model_name='mascota',
            name='prox_cita',
            field=models.DateField(default=datetime.date.today, verbose_name='Proxima Visita'),
        ),
        migrations.AlterField(
            model_name='vacuna',
            name='estado_notificacion',
            field=models.BooleanField(default=True, verbose_name='Estado de Notificación'),
        ),
        migrations.AlterField(
            model_name='vacuna',
            name='prox_cita',
            field=models.DateField(default=datetime.date.today, verbose_name='Proxima Visita'),
        ),
    ]