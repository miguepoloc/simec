# Generated by Django 2.2.10 on 2021-09-29 16:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0008_datos_integrante_datos_riesgo_datos_vivienda'),
    ]

    operations = [
        migrations.AddField(
            model_name='datos_integrante',
            name='vivienda',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='api.Datos_Vivienda'),
        ),
    ]
