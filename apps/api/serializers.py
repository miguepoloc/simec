from rest_framework import serializers
from .models import *


class Tipo_MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Municipio
        fields = '__all__'


class Tipo_Centro_PobladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Centro_Poblado
        fields = '__all__'


class DepartamentoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Departamento
        fields = '__all__'


class MunicipioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Municipio
        fields = '__all__'


class Centro_PobladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Centro_Poblado
        fields = '__all__'


class ZonaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Zona
        fields = '__all__'


class Tipo_Salida_De_CampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Salida_De_Campo
        fields = '__all__'


class PersonalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Personal
        fields = '__all__'


class EquipoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Equipo
        fields = '__all__'


class Salidas_De_CampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Salidas_De_Campo
        fields = '__all__'


class Calendario_Salidas_De_CampoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendario_Salidas_De_Campo
        fields = '__all__'


class Datos_ViviendaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datos_Vivienda
        fields = '__all__'


class Datos_IntegranteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datos_Integrante
        fields = '__all__'


class Datos_RiesgoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Datos_Riesgo
        fields = '__all__'
