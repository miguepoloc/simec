# Generated by Django 2.2.10 on 2021-10-25 04:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0009_datos_integrante_vivienda'),
    ]

    operations = [
        migrations.CreateModel(
            name='ADULTO',
            fields=[
                ('COD', models.IntegerField(primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='ATENCION_A_MUJER',
            fields=[
                ('COD', models.IntegerField(primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='CENTROS_POBLADOS',
            fields=[
                ('codigo_centro_poblado', models.IntegerField(primary_key=True, serialize=False)),
                ('COD_MUNICIPIO', models.IntegerField()),
                ('CODIGO', models.IntegerField()),
                ('CENTRO_POBLADO', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['codigo_centro_poblado'],
            },
        ),
        migrations.CreateModel(
            name='Discapacidad',
            fields=[
                ('COD', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='DISCAPACIDAD2',
            fields=[
                ('COD', models.IntegerField(primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='ESCOLARIDAD',
            fields=[
                ('COD', models.IntegerField(primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='Estado_Civil',
            fields=[
                ('COD', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='Genero',
            fields=[
                ('COD', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='GESTANTES',
            fields=[
                ('COD', models.IntegerField(primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='Grupo_Etnico',
            fields=[
                ('COD', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='Hecho_Victimizante',
            fields=[
                ('COD', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='INFECCIOSAS',
            fields=[
                ('COD', models.IntegerField(primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='MUNICIPIOS',
            fields=[
                ('CODIGO', models.IntegerField(primary_key=True, serialize=False)),
                ('MUNICIPIO', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['CODIGO'],
            },
        ),
        migrations.CreateModel(
            name='Ocupacion',
            fields=[
                ('COD', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='Orientacion_Sexual',
            fields=[
                ('COD', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='PARENEZCOS',
            fields=[
                ('CODIGO', models.AutoField(primary_key=True, serialize=False)),
                ('PARENTEXCO', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-CODIGO'],
            },
        ),
        migrations.CreateModel(
            name='RAZON_DE_ABANDONO_ESCOLAR',
            fields=[
                ('COD', models.IntegerField(primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='RIESGO_PARA_LA_INFANCIA',
            fields=[
                ('COD', models.IntegerField(primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='RIESGOS_PSICOSOCIALES',
            fields=[
                ('COD', models.IntegerField(primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='SALUD_ORAL',
            fields=[
                ('COD', models.IntegerField(primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='SEGURIDAD_ALIMENTARIA_Y_NUTRICIONAL',
            fields=[
                ('COD', models.IntegerField(primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=500, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='Sexo',
            fields=[
                ('COD', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='Tipo_Afiliacion',
            fields=[
                ('COD', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.CreateModel(
            name='TIPOS_VIVIENDA',
            fields=[
                ('CODIGO', models.AutoField(primary_key=True, serialize=False)),
                ('TIPO', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-CODIGO'],
            },
        ),
        migrations.CreateModel(
            name='Vinculacion_SGSSS',
            fields=[
                ('COD', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('DETALLE', models.CharField(blank=True, max_length=100, null=True)),
            ],
            options={
                'ordering': ['-COD'],
            },
        ),
        migrations.RemoveField(
            model_name='municipio',
            name='departamento',
        ),
        migrations.RemoveField(
            model_name='municipio',
            name='tipo_municipio',
        ),
        migrations.DeleteModel(
            name='Centro_Poblado',
        ),
        migrations.DeleteModel(
            name='Municipio',
        ),
    ]
