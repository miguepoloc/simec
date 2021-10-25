from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Tipo_Municipio',
                views.Tipo_MunicipioViewSet, "Tipo_Municipio")
router.register(r'Tipo_Centro_Poblado',
                views.Tipo_Centro_PobladoViewSet, "Tipo_Centro_Poblado")
router.register(r'Departamento', views.DepartamentoViewSet, "Departamento")
router.register(r'Municipio', views.MunicipioViewSet, "Municipio")
router.register(r'Centro_Poblado',
                views.Centro_PobladoViewSet, "Centro_Poblado")
router.register(r'Zona', views.ZonaViewSet, "Zona")
router.register(r'Tipo_Salida_De_Campo',
                views.Tipo_Salida_De_CampoViewSet, "Tipo_Salida_De_Campo")
router.register(r'Personal', views.PersonalViewSet, "Personal")
router.register(r'Equipo', views.EquipoViewSet, "Equipo")
router.register(r'Salida_De_Campo',
                views.Salidas_De_CampoViewSet, "Salida_De_Campo")
router.register(r'Calendario_Salida_De_Campo',
                views.Calendario_Salidas_De_CampoViewSet, "Calendario_Salida_De_Campo")
router.register(r'PARENEZCOS',
                views.PARENEZCOSViewSet, "PARENEZCOS")
router.register(r'TIPOS_VIVIENDA',
                views.TIPOS_VIVIENDAViewSet, "TIPOS_VIVIENDA")
router.register(r'Sexo',
                views.SexoViewSet, "Sexo")
router.register(r'Genero',
                views.GeneroViewSet, "Genero")
router.register(r'Orientacion_Sexual',
                views.Orientacion_SexualViewSet, "Orientacion_Sexual")
router.register(r'Estado_Civil',
                views.Estado_CivilViewSet, "Estado_Civil")
router.register(r'Ocupacion',
                views.OcupacionViewSet, "Ocupacion")
router.register(r'Discapacidad',
                views.DiscapacidadViewSet, "Discapacidad")
router.register(r'Grupo_Etnico',
                views.Grupo_EtnicoViewSet, "Grupo_Etnico")
router.register(r'Hecho_Victimizante',
                views.Hecho_VictimizanteViewSet, "Hecho_Victimizante")
router.register(r'Vinculacion_SGSSS',
                views.Vinculacion_SGSSSViewSet, "Vinculacion_SGSSS")
router.register(r'Tipo_Afiliacion',
                views.Tipo_AfiliacionViewSet, "Tipo_Afiliacion")
router.register(r'ESCOLARIDAD',
                views.ESCOLARIDADViewSet, "ESCOLARIDAD")
router.register(r'RAZON_DE_ABANDONO_ESCOLAR',
                views.RAZON_DE_ABANDONO_ESCOLARViewSet, "RAZON_DE_ABANDONO_ESCOLAR")
router.register(r'DISCAPACIDAD2',
                views.DISCAPACIDAD2ViewSet, "DISCAPACIDAD2")
router.register(r'RIESGOS_PSICOSOCIALES',
                views.RIESGOS_PSICOSOCIALESViewSet, "RIESGOS_PSICOSOCIALES")
router.register(r'RIESGO_PARA_LA_INFANCIA',
                views.RIESGO_PARA_LA_INFANCIAViewSet, "RIESGO_PARA_LA_INFANCIA")
router.register(r'ATENCION_A_MUJER',
                views.ATENCION_A_MUJERViewSet, "ATENCION_A_MUJER")
router.register(r'GESTANTES',
                views.GESTANTESViewSet, "GESTANTES")
router.register(r'ADULTO',
                views.ADULTOViewSet, "ADULTO")
router.register(r'INFECCIOSAS',
                views.INFECCIOSASViewSet, "INFECCIOSAS")
router.register(r'SALUD_ORAL',
                views.SALUD_ORALViewSet, "SALUD_ORAL")
router.register(r'SEGURIDAD_ALIMENTARIA_Y_NUTRICIONAL',
                views.SEGURIDAD_ALIMENTARIA_Y_NUTRICIONALViewSet, "SEGURIDAD_ALIMENTARIA_Y_NUTRICIONAL")
router.register(r'Datos_Vivienda',
                views.Datos_ViviendaViewSet, "Datos_Vivienda")
router.register(r'Datos_Integrante',
                views.Datos_IntegranteViewSet, "Datos_Integrante")
router.register(r'Datos_Riesgo',
                views.Datos_RiesgoViewSet, "Datos_Riesgo")


urlpatterns = [
    path('', include(router.urls)),
]
