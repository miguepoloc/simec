from django.shortcuts import render
from rest_framework import views, viewsets, mixins
from rest_framework.response import Response
from .serializers import *
from .models import *


class Tipo_MunicipioViewSet(viewsets.ModelViewSet):

    queryset = Tipo_Municipio.objects.all().order_by('id')
    serializer_class = Tipo_MunicipioSerializer


class Tipo_Centro_PobladoViewSet(viewsets.ModelViewSet):

    queryset = Tipo_Centro_Poblado.objects.all().order_by('id')
    serializer_class = Tipo_Centro_PobladoSerializer


class DepartamentoViewSet(viewsets.ModelViewSet):

    queryset = Departamento.objects.all().order_by('codigo_departamento')
    serializer_class = DepartamentoSerializer


class MunicipioViewSet(viewsets.ModelViewSet):

    queryset = MUNICIPIOS.objects.all().order_by('codigo_municipio')
    serializer_class = MunicipioSerializer


class Centro_PobladoViewSet(viewsets.ModelViewSet):

    queryset = CENTROS_POBLADOS.objects.all().order_by('codigo_centro_poblado')
    serializer_class = Centro_PobladoSerializer


class ZonaViewSet(viewsets.ModelViewSet):

    queryset = Zona.objects.all().order_by('id')
    serializer_class = ZonaSerializer


class Tipo_Salida_De_CampoViewSet(viewsets.ModelViewSet):

    queryset = Tipo_Salida_De_Campo.objects.all().order_by('id')
    serializer_class = Tipo_Salida_De_CampoSerializer


class PersonalViewSet(viewsets.ModelViewSet):

    queryset = Personal.objects.all().order_by('id')
    serializer_class = PersonalSerializer


class EquipoViewSet(viewsets.ModelViewSet):

    queryset = Equipo.objects.all().order_by('id')
    serializer_class = EquipoSerializer


class Salidas_De_CampoViewSet(viewsets.ModelViewSet):

    queryset = Salidas_De_Campo.objects.all().order_by('-fecha')
    serializer_class = Salidas_De_CampoSerializer


class Calendario_Salidas_De_CampoViewSet(viewsets.ModelViewSet):

    queryset = Calendario_Salidas_De_Campo.objects.all().order_by('-fecha_inicio')
    serializer_class = Calendario_Salidas_De_CampoSerializer


class PARENEZCOSViewSet(viewsets.ModelViewSet):

    queryset = PARENEZCOS.objects.all().order_by('-CODIGO')
    serializer_class = PARENEZCOSSerializer


class TIPOS_VIVIENDAViewSet(viewsets.ModelViewSet):

    queryset = TIPOS_VIVIENDA.objects.all().order_by('-CODIGO')
    serializer_class = TIPOS_VIVIENDASerializer


class SexoViewSet(viewsets.ModelViewSet):

    queryset = Sexo.objects.all().order_by('-COD')
    serializer_class = SexoSerializer


class GeneroViewSet(viewsets.ModelViewSet):

    queryset = Genero.objects.all().order_by('-COD')
    serializer_class = GeneroSerializer


class Orientacion_SexualViewSet(viewsets.ModelViewSet):

    queryset = Orientacion_Sexual.objects.all().order_by('-COD')
    serializer_class = Orientacion_SexualSerializer


class Estado_CivilViewSet(viewsets.ModelViewSet):

    queryset = Estado_Civil.objects.all().order_by('-COD')
    serializer_class = Estado_CivilSerializer


class OcupacionViewSet(viewsets.ModelViewSet):

    queryset = Ocupacion.objects.all().order_by('-COD')
    serializer_class = OcupacionSerializer


class DiscapacidadViewSet(viewsets.ModelViewSet):

    queryset = Discapacidad.objects.all().order_by('-COD')
    serializer_class = DiscapacidadSerializer


class Grupo_EtnicoViewSet(viewsets.ModelViewSet):

    queryset = Grupo_Etnico.objects.all().order_by('-COD')
    serializer_class = Grupo_EtnicoSerializer


class Hecho_VictimizanteViewSet(viewsets.ModelViewSet):

    queryset = Hecho_Victimizante.objects.all().order_by('-COD')
    serializer_class = Hecho_VictimizanteSerializer


class Vinculacion_SGSSSViewSet(viewsets.ModelViewSet):

    queryset = Vinculacion_SGSSS.objects.all().order_by('-COD')
    serializer_class = Vinculacion_SGSSSSerializer


class Tipo_AfiliacionViewSet(viewsets.ModelViewSet):

    queryset = Tipo_Afiliacion.objects.all().order_by('-COD')
    serializer_class = Tipo_AfiliacionSerializer


class ESCOLARIDADViewSet(viewsets.ModelViewSet):

    queryset = ESCOLARIDAD.objects.all().order_by('-COD')
    serializer_class = ESCOLARIDADSerializer


class RAZON_DE_ABANDONO_ESCOLARViewSet(viewsets.ModelViewSet):

    queryset = RAZON_DE_ABANDONO_ESCOLAR.objects.all().order_by('-COD')
    serializer_class = RAZON_DE_ABANDONO_ESCOLARSerializer


class DISCAPACIDAD2ViewSet(viewsets.ModelViewSet):

    queryset = DISCAPACIDAD2.objects.all().order_by('-COD')
    serializer_class = DISCAPACIDAD2Serializer


class RIESGOS_PSICOSOCIALESViewSet(viewsets.ModelViewSet):

    queryset = RIESGOS_PSICOSOCIALES.objects.all().order_by('-COD')
    serializer_class = RIESGOS_PSICOSOCIALESSerializer


class RIESGO_PARA_LA_INFANCIAViewSet(viewsets.ModelViewSet):

    queryset = RIESGO_PARA_LA_INFANCIA.objects.all().order_by('-COD')
    serializer_class = RIESGO_PARA_LA_INFANCIASerializer


class ATENCION_A_MUJERViewSet(viewsets.ModelViewSet):

    queryset = ATENCION_A_MUJER.objects.all().order_by('-COD')
    serializer_class = ATENCION_A_MUJERSerializer


class GESTANTESViewSet(viewsets.ModelViewSet):

    queryset = GESTANTES.objects.all().order_by('-COD')
    serializer_class = GESTANTESSerializer


class ADULTOViewSet(viewsets.ModelViewSet):

    queryset = ADULTO.objects.all().order_by('-COD')
    serializer_class = ADULTOSerializer


class INFECCIOSASViewSet(viewsets.ModelViewSet):

    queryset = INFECCIOSAS.objects.all().order_by('-COD')
    serializer_class = INFECCIOSASSerializer


class SALUD_ORALViewSet(viewsets.ModelViewSet):

    queryset = SALUD_ORAL.objects.all().order_by('-COD')
    serializer_class = SALUD_ORALSerializer


class SEGURIDAD_ALIMENTARIA_Y_NUTRICIONALViewSet(viewsets.ModelViewSet):

    queryset = SEGURIDAD_ALIMENTARIA_Y_NUTRICIONAL.objects.all().order_by('-COD')
    serializer_class = SEGURIDAD_ALIMENTARIA_Y_NUTRICIONALSerializer


class Datos_ViviendaViewSet(viewsets.ModelViewSet):

    queryset = Datos_Vivienda.objects.all().order_by('-nro_ficha')
    serializer_class = Datos_ViviendaSerializer


class Datos_IntegranteViewSet(viewsets.ModelViewSet):

    queryset = Datos_Integrante.objects.all().order_by('-identif')
    serializer_class = Datos_IntegranteSerializer


class Datos_RiesgoViewSet(viewsets.ModelViewSet):

    queryset = Datos_Riesgo.objects.all().order_by('-identif')
    serializer_class = Datos_RiesgoSerializer
