from rest_framework import serializers
from .models import (Zona, Tipo_Salida_De_Campo, Personal,
                     Salidas_De_Campo, Calendario_Salidas_De_Campo, Equipo)


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
