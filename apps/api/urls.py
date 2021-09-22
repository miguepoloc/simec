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
router.register(r'Datos_Vivienda',
                views.Datos_ViviendaViewSet, "Datos_Vivienda")
router.register(r'Datos_Integrante',
                views.Datos_IntegranteViewSet, "Datos_Integrante")
router.register(r'Datos_Riesgo',
                views.Datos_RiesgoViewSet, "Datos_Riesgo")


urlpatterns = [
    path('', include(router.urls)),
]
