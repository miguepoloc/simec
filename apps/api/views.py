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

    queryset = Municipio.objects.all().order_by('codigo_municipio')
    serializer_class = MunicipioSerializer


class Centro_PobladoViewSet(viewsets.ModelViewSet):

    queryset = Centro_Poblado.objects.all().order_by('codigo_centro_poblado')
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


class Datos_ViviendaViewSet(viewsets.ModelViewSet):

    queryset = Datos_Vivienda.objects.all().order_by('-nro_ficha')
    serializer_class = Datos_ViviendaSerializer


class Datos_IntegranteViewSet(viewsets.ModelViewSet):

    queryset = Datos_Integrante.objects.all().order_by('-identif')
    serializer_class = Datos_IntegranteSerializer


class Datos_RiesgoViewSet(viewsets.ModelViewSet):

    queryset = Datos_Riesgo.objects.all().order_by('-identif')
    serializer_class = Datos_RiesgoSerializer
