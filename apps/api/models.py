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


class MUNICIPIOS(models.Model):
    """
    Una clase que define el modelo de los municipios
    """
    # Campos
    CODIGO = models.IntegerField(primary_key=True)
    MUNICIPIO = models.CharField(max_length=100)

    # Metadata
    class Meta:
        ordering = ["CODIGO"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('municipio_detail', args=[str(self.CODIGO)])

    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return self.MUNICIPIO


class CENTROS_POBLADOS(models.Model):
    """
    Una clase que define el modelo de los municipios
    """
    # Campos
    codigo_centro_poblado = models.IntegerField(primary_key=True)
    COD_MUNICIPIO = models.IntegerField()
    CODIGO = models.IntegerField()
    CENTRO_POBLADO = models.CharField(max_length=100)

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
        return self.CENTRO_POBLADO


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


class PARENEZCOS(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    CODIGO = models.AutoField(primary_key=True)
    PARENTEXCO = models.CharField(max_length=100, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-CODIGO"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.CODIGO)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.PARENTEXCO)


class TIPOS_VIVIENDA(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    CODIGO = models.AutoField(primary_key=True)
    TIPO = models.CharField(max_length=100, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-CODIGO"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.CODIGO)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.TIPO)


class Sexo(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.CharField(max_length=100, primary_key=True)
    DETALLE = models.CharField(max_length=100, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class Genero(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.CharField(max_length=100, primary_key=True)
    DETALLE = models.CharField(max_length=100, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class Orientacion_Sexual(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.CharField(max_length=100, primary_key=True)
    DETALLE = models.CharField(max_length=100, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class Estado_Civil(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.CharField(max_length=100, primary_key=True)
    DETALLE = models.CharField(max_length=100, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class Ocupacion(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.CharField(max_length=100, primary_key=True)
    DETALLE = models.CharField(max_length=100, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class Discapacidad(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.CharField(max_length=100, primary_key=True)
    DETALLE = models.CharField(max_length=100, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class Grupo_Etnico(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.CharField(max_length=100, primary_key=True)
    DETALLE = models.CharField(max_length=100, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class Hecho_Victimizante(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.CharField(max_length=100, primary_key=True)
    DETALLE = models.CharField(max_length=100, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class Vinculacion_SGSSS(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.CharField(max_length=100, primary_key=True)
    DETALLE = models.CharField(max_length=100, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class Tipo_Afiliacion(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.CharField(max_length=100, primary_key=True)
    DETALLE = models.CharField(max_length=100, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class ESCOLARIDAD(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.IntegerField(primary_key=True)
    DETALLE = models.CharField(max_length=100, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class RAZON_DE_ABANDONO_ESCOLAR(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.IntegerField(primary_key=True)
    DETALLE = models.CharField(max_length=100, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class DISCAPACIDAD2(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.IntegerField(primary_key=True)
    DETALLE = models.CharField(max_length=100, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class RIESGOS_PSICOSOCIALES(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.IntegerField(primary_key=True)
    DETALLE = models.CharField(max_length=100, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class RIESGO_PARA_LA_INFANCIA(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.IntegerField(primary_key=True)
    DETALLE = models.CharField(max_length=500, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class ATENCION_A_MUJER(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.IntegerField(primary_key=True)
    DETALLE = models.CharField(max_length=500, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class GESTANTES(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.IntegerField(primary_key=True)
    DETALLE = models.CharField(max_length=500, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class ADULTO(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.IntegerField(primary_key=True)
    DETALLE = models.CharField(max_length=500, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class INFECCIOSAS(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.IntegerField(primary_key=True)
    DETALLE = models.CharField(max_length=500, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class SALUD_ORAL(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.IntegerField(primary_key=True)
    DETALLE = models.CharField(max_length=500, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class SEGURIDAD_ALIMENTARIA_Y_NUTRICIONAL(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    COD = models.IntegerField(primary_key=True)
    DETALLE = models.CharField(max_length=500, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-COD"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.COD)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.DETALLE)


class Datos_Vivienda(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    uid = models.BigIntegerField(primary_key=True)
    MunicipioVivienda = models.ForeignKey(
        'MUNICIPIOS', on_delete=models.SET_NULL, null=True, blank=True)
    CentroPoblado = models.ForeignKey(
        'CENTROS_POBLADOS', on_delete=models.SET_NULL, null=True, blank=True)
    DirVivienda = models.CharField(max_length=100, blank=True, null=True)
    BarrioVivienda = models.CharField(max_length=100, blank=True, null=True)
    GeoLocate = models.CharField(max_length=100, blank=True, null=True)
    ParentezcoRecibeVisita = models.ForeignKey(
        'PARENEZCOS', on_delete=models.SET_NULL, null=True, blank=True)
    NombreRecibeVisita = models.CharField(
        max_length=100, blank=True, null=True)
    TDRecibeVisita = models.CharField(max_length=100, blank=True, null=True)
    IdentcoRecibeVisita = models.BigIntegerField(blank=True, null=True)
    FnacRecibeVisita = models.DateField(max_length=2000, blank=True, null=True)
    TelRecibeVisita = models.BigIntegerField(blank=True, null=True)
    ParentezcoRecibeVisita = models.ForeignKey(
        'TIPOS_VIVIENDA', on_delete=models.SET_NULL, null=True, blank=True)
    NombreOtroTipoVivienda = models.CharField(
        max_length=100, blank=True, null=True)
    NroPersonasVivienda = models.IntegerField(blank=True, null=True)
    NroDormitoriosVivienda = models.IntegerField(blank=True, null=True)
    PerrosEnVivienda = models.IntegerField(blank=True, null=True)
    GatosEnVivienda = models.IntegerField(blank=True, null=True)
    OtrasMascotasEnVivienda = models.IntegerField(blank=True, null=True)
    PerrosNoVacunEnVivienda = models.IntegerField(blank=True, null=True)
    GatosNoVacunEnVivienda = models.IntegerField(blank=True, null=True)
    TenenciaBovinos = models.IntegerField(blank=True, null=True)
    TenenciaCaprinos = models.IntegerField(blank=True, null=True)
    TenenciaOvinos = models.IntegerField(blank=True, null=True)
    TenenciaPorcinos = models.IntegerField(blank=True, null=True)
    TenenciaEquinos = models.IntegerField(blank=True, null=True)
    TenenciaEMenores = models.IntegerField(blank=True, null=True)
    TenenciaAExoticos = models.IntegerField(blank=True, null=True)
    OtrosAnimalesTenencia = models.IntegerField(blank=True, null=True)
    riesgoVivEV01 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivEV02 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivEV03 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivEV04 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivEV05 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivEV06 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivEV07 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivEV08 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivCA01 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivCA02 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivCA03 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivCA04 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivMA01 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivMA02 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivMA03 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivRS01 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivRS02 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivRS03 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivRS04 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivRS05 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivRS06 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivRS07 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivMP01 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivMP02 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivMP03 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivAH01 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivAH02 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivAH03 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivAH04 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivAH05 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivCR01 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivCR02 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivCR03 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivCR04 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivCR05 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivCR06 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivCR07 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivCR08 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivNM01 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivNM02 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivNM03 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivNM04 = models.CharField(max_length=100, blank=True, null=True)
    riesgoVivNM05 = models.CharField(max_length=100, blank=True, null=True)
    subsidioVivienda = models.CharField(max_length=100, blank=True, null=True)

    # Metadata
    class Meta:
        ordering = ["-uid"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('Datos_Vivienda_detail', args=[str(self.uid)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s (%s)' % (self.NombreRecibeVisita, self.uid)


class Datos_Integrante(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    identif = models.BigIntegerField(primary_key=True)
    vivienda = models.ForeignKey(
        'Datos_Vivienda', on_delete=models.SET_NULL, null=True, blank=True)
    nombre = models.CharField(max_length=100, blank=True, null=True)
    tipoid = models.CharField(max_length=100, blank=True, null=True)
    fnac = models.DateField(max_length=2000, blank=True, null=True)
    paren = models.CharField(max_length=100, blank=True, null=True)
    sx = models.CharField(max_length=100, blank=True, null=True)
    gen = models.CharField(max_length=100, blank=True, null=True)
    osex = models.CharField(max_length=100, blank=True, null=True)
    ecivil = models.CharField(max_length=100, blank=True, null=True)
    ocup = models.CharField(max_length=100, blank=True, null=True)
    disc = models.CharField(max_length=100, blank=True, null=True)
    etnia = models.CharField(max_length=100, blank=True, null=True)
    victima = models.CharField(max_length=100, blank=True, null=True)
    sgss = models.CharField(max_length=100, blank=True, null=True)
    afi = models.CharField(max_length=100, blank=True, null=True)

    # Metadata
    class Meta:
        ordering = ["-identif"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('integrante_detail', args=[str(self.identif)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s (%s)' % (self.nombre, self.identif)


class Datos_Riesgo(models.Model):
    """
    Una clase que define el modelo de las salidas de campo
    """
    # Campos
    id = models.AutoField(primary_key=True)
    identif = models.ForeignKey(
        'Datos_Integrante', on_delete=models.SET_NULL, null=True, blank=True)
    op01 = models.CharField(max_length=100, blank=True, null=True)
    op02 = models.CharField(max_length=100, blank=True, null=True)
    op03 = models.CharField(max_length=100, blank=True, null=True)
    op04 = models.CharField(max_length=100, blank=True, null=True)
    op05 = models.CharField(max_length=100, blank=True, null=True)
    op06 = models.CharField(max_length=100, blank=True, null=True)
    op07 = models.CharField(max_length=100, blank=True, null=True)
    op08 = models.CharField(max_length=100, blank=True, null=True)
    op09 = models.CharField(max_length=100, blank=True, null=True)
    op10 = models.CharField(max_length=100, blank=True, null=True)
    op11 = models.CharField(max_length=100, blank=True, null=True)

    # Metadata

    class Meta:
        ordering = ["-identif"]

    # Métodos
    def get_absolute_url(self):
        """
        Devuelve la url para acceder a una instancia particular de MyModelName.
        """
        return reverse('riesgo_detail', args=[str(self.identif)])

    # Nombre
    def __str__(self):
        """
        Cadena para representar el objeto en el sitio de Admin
        """
        return '%s' % (self.identif)
