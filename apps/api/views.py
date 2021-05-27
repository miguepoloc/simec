from django.shortcuts import render
from rest_framework import views, viewsets, mixins
from rest_framework.response import Response
from .serializers import (ZonaSerializer, Tipo_Salida_De_CampoSerializer, PersonalSerializer, Salidas_De_CampoSerializer,
                          Calendario_Salidas_De_CampoSerializer, EquipoSerializer)
from .models import (Zona, Tipo_Salida_De_Campo, Personal, Equipo,
                     Salidas_De_Campo, Calendario_Salidas_De_Campo)


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
