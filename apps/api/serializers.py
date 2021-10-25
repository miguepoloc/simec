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
        model = MUNICIPIOS
        fields = '__all__'


class Centro_PobladoSerializer(serializers.ModelSerializer):
    class Meta:
        model = CENTROS_POBLADOS
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


class PARENEZCOSSerializer(serializers.ModelSerializer):
    class Meta:
        model = PARENEZCOS
        fields = '__all__'


class TIPOS_VIVIENDASerializer(serializers.ModelSerializer):
    class Meta:
        model = TIPOS_VIVIENDA
        fields = '__all__'


class SexoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sexo
        fields = '__all__'


class GeneroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genero
        fields = '__all__'


class Orientacion_SexualSerializer(serializers.ModelSerializer):
    class Meta:
        model = Orientacion_Sexual
        fields = '__all__'


class Estado_CivilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estado_Civil
        fields = '__all__'


class OcupacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ocupacion
        fields = '__all__'


class DiscapacidadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discapacidad
        fields = '__all__'


class Grupo_EtnicoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Grupo_Etnico
        fields = '__all__'


class Hecho_VictimizanteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Hecho_Victimizante
        fields = '__all__'


class Vinculacion_SGSSSSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vinculacion_SGSSS
        fields = '__all__'


class Tipo_AfiliacionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tipo_Afiliacion
        fields = '__all__'


class ESCOLARIDADSerializer(serializers.ModelSerializer):
    class Meta:
        model = ESCOLARIDAD
        fields = '__all__'


class RAZON_DE_ABANDONO_ESCOLARSerializer(serializers.ModelSerializer):
    class Meta:
        model = RAZON_DE_ABANDONO_ESCOLAR
        fields = '__all__'


class DISCAPACIDAD2Serializer(serializers.ModelSerializer):
    class Meta:
        model = DISCAPACIDAD2
        fields = '__all__'


class RIESGOS_PSICOSOCIALESSerializer(serializers.ModelSerializer):
    class Meta:
        model = RIESGOS_PSICOSOCIALES
        fields = '__all__'


class RIESGO_PARA_LA_INFANCIASerializer(serializers.ModelSerializer):
    class Meta:
        model = RIESGO_PARA_LA_INFANCIA
        fields = '__all__'


class ATENCION_A_MUJERSerializer(serializers.ModelSerializer):
    class Meta:
        model = ATENCION_A_MUJER
        fields = '__all__'


class GESTANTESSerializer(serializers.ModelSerializer):
    class Meta:
        model = GESTANTES
        fields = '__all__'


class ADULTOSerializer(serializers.ModelSerializer):
    class Meta:
        model = ADULTO
        fields = '__all__'


class INFECCIOSASSerializer(serializers.ModelSerializer):
    class Meta:
        model = INFECCIOSAS
        fields = '__all__'


class SALUD_ORALSerializer(serializers.ModelSerializer):
    class Meta:
        model = SALUD_ORAL
        fields = '__all__'


class SEGURIDAD_ALIMENTARIA_Y_NUTRICIONALSerializer(serializers.ModelSerializer):
    class Meta:
        model = SEGURIDAD_ALIMENTARIA_Y_NUTRICIONAL
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
