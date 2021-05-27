from django.urls import include, path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'Zona', views.ZonaViewSet, "Zona")
router.register(r'Tipo_Salida_De_Campo',
                views.Tipo_Salida_De_CampoViewSet, "Tipo_Salida_De_Campo")
router.register(r'Personal', views.PersonalViewSet, "Personal")
router.register(r'Equipo', views.EquipoViewSet, "Equipo")
router.register(r'Salida_De_Campo',
                views.Salidas_De_CampoViewSet, "Salida_De_Campo")
router.register(r'Calendario_Salida_De_Campo',
                views.Calendario_Salidas_De_CampoViewSet, "Calendario_Salida_De_Campo")


urlpatterns = [
    path('', include(router.urls)),
]
