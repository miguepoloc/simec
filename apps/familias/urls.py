from django.urls import path
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    url(r'^$', views.FamiliasListView.as_view(), name='familias'),
    url(r'^(?P<pk>\d+)$', views.FamiliasDetailView.as_view(),
        name='Datos_Vivienda_detail'),
    url(r'^integrante/(?P<pk>\d+)$', views.DatosIntegranteDetailView.as_view(),
        name='integrante_detail'),
]
