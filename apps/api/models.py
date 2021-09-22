from typing import no_type_check
from django.urls import reverse
from django.db import models
from django.utils import timezone


def corrector_hora():
    return str(timezone.now() + timezone.timedelta(hours=-5)).split(".")[0]


class Tipo_Municipio(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(
        max_length=200, help_text="Ingrese el tipo de municipio")
    color = models.CharField(max_length=100, blank=True, null=True)
    simbolo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return self.tipo


class Tipo_Centro_Poblado(models.Model):
    id = models.AutoField(primary_key=True)
    codigo = models.CharField(
        max_length=200, help_text="Ingrese el código del centro poblado")
    tipo = models.CharField(
        max_length=200, help_text="Ingrese el tipo de centro poblado")
    color = models.CharField(max_length=100, blank=True, null=True)
    simbolo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return self.tipo


class Departamento(models.Model):
    """
    Una clase que define el modelo de los departamentos
    """
    # Campos
    codigo_departamento = models.IntegerField(primary_key=True)
    nombre_departamento = models.CharField(max_length=100)

    # Metadata
    class Meta:
        ordering = ["codigo_departamento"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('departamento_detail', args=[str(self.codigo_departamento)])

    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return self.nombre_departamento


class Municipio(models.Model):
    """
    Una clase que define el modelo de los municipios
    """
    # Campos
    codigo_municipio = models.IntegerField(primary_key=True)
    nombre_municipio = models.CharField(max_length=100)
    departamento = models.ForeignKey(
        'Departamento', on_delete=models.SET_NULL, null=True, blank=True)
    tipo_municipio = models.ForeignKey(
        'Tipo_Municipio', on_delete=models.SET_NULL, null=True, blank=True)

    # Metadata
    class Meta:
        ordering = ["codigo_municipio"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('municipio_detail', args=[str(self.codigo_municipio)])

    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return self.nombre_municipio


class Centro_Poblado(models.Model):
    """
    Una clase que define el modelo de los municipios
    """
    # Campos
    codigo_centro_poblado = models.IntegerField(primary_key=True)
    nombre_centro_poblado = models.CharField(max_length=100)
    municipio = models.ForeignKey(
        'Municipio', on_delete=models.SET_NULL, null=True, blank=True)
    departamento = models.ForeignKey(
        'Departamento', on_delete=models.SET_NULL, null=True, blank=True)
    tipo_centro_poblado = models.ForeignKey(
        'Tipo_Centro_Poblado', on_delete=models.SET_NULL, null=True, blank=True)

    # Metadata
    class Meta:
        ordering = ["codigo_centro_poblado"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('centro_poblado_detail', args=[str(self.codigo_centro_poblado)])

    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return self.nombre_centro_poblado


class Zona(models.Model):
    """
    Una clase que define el modelo de las estaciones
    """
    # Campos
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100)
    latitud = models.FloatField(blank=True, null=True)
    longitud = models.FloatField(blank=True, null=True)
    sitio = models.CharField(max_length=4000, blank=True, null=True)
    descripcion = models.CharField(max_length=4000, blank=True, null=True)
    observaciones = models.TextField(max_length=4000, blank=True, null=True)
    color = models.CharField(
        max_length=200, help_text="Ingrese el color en formato Hexa", null=True, blank=True)

    # Metadata
    class Meta:
        ordering = ["id"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('zona_detail', args=[str(self.id)])

    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return self.nombre


class Tipo_Salida_De_Campo(models.Model):
    id = models.AutoField(primary_key=True)
    tipo = models.CharField(
        max_length=200, help_text="Ingrese el tipo de salida de campo")
    color = models.CharField(max_length=100, blank=True, null=True)
    requerimientos = models.CharField(max_length=100, blank=True, null=True)
    simbolo = models.CharField(max_length=100)

    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return self.tipo


class Personal(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(
        max_length=200, help_text="Ingrese el nombre completo")
    cedula = models.BigIntegerField(blank=True, null=True)
    telefono = models.BigIntegerField(blank=True, null=True)
    cargo = models.CharField(max_length=100, blank=True, null=True)
    correo = models.CharField(max_length=100, blank=True, null=True)

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular
        """
        return reverse('personal_detail', args=[str(self.id)])

    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return self.nombre


class Equipo(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=200)
    medico = models.ForeignKey(
        'Personal', on_delete=models.SET_NULL, null=True, blank=True, related_name='medico')
    enfermero_jefe = models.ForeignKey(
        'Personal', on_delete=models.SET_NULL, null=True, blank=True, related_name='enfermero_jefe')
    auxiliar_enfermeria_1 = models.ForeignKey(
        'Personal', on_delete=models.SET_NULL, null=True, blank=True, related_name='auxiliar_enfermeria1')
    auxiliar_enfermeria_2 = models.ForeignKey(
        'Personal', on_delete=models.SET_NULL, null=True, blank=True, related_name='auxiliar_enfermeria2')
    auxiliar_enfermeria_3 = models.ForeignKey(
        'Personal', on_delete=models.SET_NULL, null=True, blank=True, related_name='auxiliar_enfermeria3')
    auxiliar_enfermeria_4 = models.ForeignKey(
        'Personal', on_delete=models.SET_NULL, null=True, blank=True, related_name='auxiliar_enfermeria4')
    auxiliar_enfermeria_5 = models.ForeignKey(
        'Personal', on_delete=models.SET_NULL, null=True, blank=True, related_name='auxiliar_enfermeria5')
    auxiliar_enfermeria_6 = models.ForeignKey(
        'Personal', on_delete=models.SET_NULL, null=True, blank=True, related_name='auxiliar_enfermeria6')
    auxiliar_enfermeria_7 = models.ForeignKey(
        'Personal', on_delete=models.SET_NULL, null=True, blank=True, related_name='auxiliar_enfermeria7')
    tecnico_ambiental = models.ForeignKey(
        'Personal', on_delete=models.SET_NULL, null=True, blank=True, related_name='tecnico_ambiental')
    psicologo = models.ForeignKey(
        'Personal', on_delete=models.SET_NULL, null=True, blank=True, related_name='psicologo')

    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('equipo_detail', args=[str(self.id)])

    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return self.nombre


class Salidas_De_Campo(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    id = models.AutoField(primary_key=True)
    zona = models.ForeignKey(
        'Zona', on_delete=models.SET_NULL, null=True, blank=True)
    fecha = models.DateField(
        max_length=2000, blank=True, null=True)
    tipo_de_salida = models.ForeignKey(
        'Tipo_Salida_De_Campo', on_delete=models.SET_NULL, null=True, blank=True)
    operario = models.ForeignKey(
        'Personal', on_delete=models.SET_NULL, null=True, blank=True)
    observaciones = models.TextField(max_length=100000, blank=True, null=True)

    # Metadata
    class Meta:
        ordering = ["-fecha"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('salidas_de_campo_detail', args=[str(self.id)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s (%s)' % (self.zona, self.fecha)


class Calendario_Salidas_De_Campo(models.Model):
    """
    Una clase que define el modelo del calendario de las salidas de campo
    """

    # Campos
    id = models.AutoField(primary_key=True)
    zona = models.ForeignKey(
        'Zona', on_delete=models.SET_NULL, null=True, blank=True)
    fecha_inicio = models.DateField(
        max_length=2000, blank=True, null=True)
    fecha_fin = models.DateField(
        max_length=2000, blank=True, null=True)
    tipo_de_salida = models.ForeignKey(
        'Tipo_Salida_De_Campo', on_delete=models.SET_NULL, null=True, blank=True)
    observaciones = models.TextField(max_length=100000, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-fecha_inicio"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('calendario_salidas_de_campo_detail', args=[str(self.id)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s (%s - %s)' % (self.zona, self.fecha_inicio, self.fecha_fin)


# class Reporte(models.Model):
#     """
#     Una clase que define el modelo del reporte
#     """

#     # Campos
#     id = models.AutoField(primary_key=True)
#     hospital = models.CharField(
#         max_length=200, help_text="Ingrese el nombre del Hospital")
#     municipio = models.ForeignKey(
#         'Municipio', on_delete=models.SET_NULL, null=True, blank=True)
#     fecha = models.DateField(
#         max_length=2000, blank=True, null=True)
#     equipos_promocion = models.IntegerField(blank=True, null=True)
#     medicina_promocion = models.IntegerField(blank=True, null=True)
#     enfermeria_promocion = models.IntegerField(blank=True, null=True)
#     auxiliar_enfermeria_promocion = models.IntegerField(blank=True, null=True)
#     psicologia_promocion = models.IntegerField(blank=True, null=True)
#     tecnico_ambiental_promocion = models.IntegerField(blank=True, null=True)
#     odontologia_promocion = models.IntegerField(blank=True, null=True)
#     nutricionista_promocion = models.IntegerField(blank=True, null=True)
#     salud_laboral_promocion = models.IntegerField(blank=True, null=True)
#     personas_promocion = models.IntegerField(blank=True, null=True)
#     viviendas_promocion = models.IntegerField(blank=True, null=True)
#     reporte_vigilancia_promocion = models.IntegerField(blank=True, null=True)
#     canalizacion_interconsulta_promocion = models.IntegerField(blank=True, null=True)
#     canalizacion_rias_promocion = models.IntegerField(blank=True, null=True)
#     canalizacion_intersectorial_promocion = models.IntegerField(blank=True, null=True)
#     canalizacion_total_promocion = models.IntegerField(blank=True, null=True)


#     # Metadata

#     class Meta:
#         ordering = ["-fecha_inicio"]

#     # Métodos
#     def get_absolute_url(self):
#         """
#         Devuelve la url para acceder a una instancia particular de MyModelName.
#         """
#         return reverse('calendario_salidas_de_campo_detail', args=[str(self.id)])

#     # Nombre
#     def __str__(self):
#         """
#         Cadena para representar el objeto en el sitio de Admin
#         """
#         return '%s (%s - %s)' % (self.zona, self.fecha_inicio, self.fecha_fin)


class Datos_Vivienda(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    nro_ficha = models.BigIntegerField(primary_key=True)
    municipio = models.CharField(max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=100, blank=True, null=True)
    cordenadas = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tide = models.CharField(max_length=100, blank=True, null=True)
    identif = models.BigIntegerField(blank=True, null=True)
    fnac = models.DateField(max_length=2000, blank=True, null=True)
    celular = models.BigIntegerField(blank=True, null=True)
    telefono = models.BigIntegerField(blank=True, null=True)
    tipov = models.CharField(max_length=100, blank=True, null=True)
    instviivi = models.CharField(max_length=100, blank=True, null=True)
    instotro = models.CharField(max_length=100, blank=True, null=True)
    personas = models.IntegerField(blank=True, null=True)
    habitaciones = models.IntegerField(blank=True, null=True)
    perros = models.IntegerField(blank=True, null=True)
    gatos = models.IntegerField(blank=True, null=True)
    otras_mascotas = models.IntegerField(blank=True, null=True)
    det_mascotas = models.IntegerField(blank=True, null=True)
    pvacuna = models.IntegerField(blank=True, null=True)
    gvacuna = models.IntegerField(blank=True, null=True)
    bovino = models.IntegerField(blank=True, null=True)
    caprino = models.IntegerField(blank=True, null=True)
    ovino = models.IntegerField(blank=True, null=True)
    porcino = models.IntegerField(blank=True, null=True)
    equino = models.IntegerField(blank=True, null=True)
    menores = models.IntegerField(blank=True, null=True)
    exoticos = models.IntegerField(blank=True, null=True)
    otros_animales = models.IntegerField(blank=True, null=True)
    det_animales = models.IntegerField(blank=True, null=True)
    ev01 = models.CharField(max_length=100, blank=True, null=True)
    ev02 = models.CharField(max_length=100, blank=True, null=True)
    ev03 = models.CharField(max_length=100, blank=True, null=True)
    ev04 = models.CharField(max_length=100, blank=True, null=True)
    ev05 = models.CharField(max_length=100, blank=True, null=True)
    ev06 = models.CharField(max_length=100, blank=True, null=True)
    ev07 = models.CharField(max_length=100, blank=True, null=True)
    ev08 = models.CharField(max_length=100, blank=True, null=True)
    ca01 = models.CharField(max_length=100, blank=True, null=True)
    ca02 = models.CharField(max_length=100, blank=True, null=True)
    ca03 = models.CharField(max_length=100, blank=True, null=True)
    ca04 = models.CharField(max_length=100, blank=True, null=True)
    ma01 = models.CharField(max_length=100, blank=True, null=True)
    ma02 = models.CharField(max_length=100, blank=True, null=True)
    ma03 = models.CharField(max_length=100, blank=True, null=True)
    rs01 = models.CharField(max_length=100, blank=True, null=True)
    rs02 = models.CharField(max_length=100, blank=True, null=True)
    rs03 = models.CharField(max_length=100, blank=True, null=True)
    rs04 = models.CharField(max_length=100, blank=True, null=True)
    rs05 = models.CharField(max_length=100, blank=True, null=True)
    rs06 = models.CharField(max_length=100, blank=True, null=True)
    rs07 = models.CharField(max_length=100, blank=True, null=True)
    mp01 = models.CharField(max_length=100, blank=True, null=True)
    mp02 = models.CharField(max_length=100, blank=True, null=True)
    mp03 = models.CharField(max_length=100, blank=True, null=True)
    ah01 = models.CharField(max_length=100, blank=True, null=True)
    ah02 = models.CharField(max_length=100, blank=True, null=True)
    ah03 = models.CharField(max_length=100, blank=True, null=True)
    ah04 = models.CharField(max_length=100, blank=True, null=True)
    ah05 = models.CharField(max_length=100, blank=True, null=True)
    cr01 = models.CharField(max_length=100, blank=True, null=True)
    cr02 = models.CharField(max_length=100, blank=True, null=True)
    cr03 = models.CharField(max_length=100, blank=True, null=True)
    cr04 = models.CharField(max_length=100, blank=True, null=True)
    cr05 = models.CharField(max_length=100, blank=True, null=True)
    cr06 = models.CharField(max_length=100, blank=True, null=True)
    cr07 = models.CharField(max_length=100, blank=True, null=True)
    cr08 = models.CharField(max_length=100, blank=True, null=True)
    nm01 = models.CharField(max_length=100, blank=True, null=True)
    nm02 = models.CharField(max_length=100, blank=True, null=True)
    nm03 = models.CharField(max_length=100, blank=True, null=True)
    nm04 = models.CharField(max_length=100, blank=True, null=True)
    nm05 = models.CharField(max_length=100, blank=True, null=True)
    subsidio = models.CharField(max_length=100, blank=True, null=True)
    nombresub = models.CharField(max_length=100, blank=True, null=True)

    # Metadata
    class Meta:
        ordering = ["-nro_ficha"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('familias_detail', args=[str(self.nro_ficha)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s (%s)' % (self.nombre, self.nro_ficha)
