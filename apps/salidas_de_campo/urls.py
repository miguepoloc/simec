from django.urls import path
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    # url(r'^$', views.Salidas_De_CampoListView.as_view(), name='salidas_de_campo'),
    url(r'^$', views.Salidas_De_CampoForm, name='salidas_de_campo'),
    # # url(r'^$', views.Salidas_De_CampoForm.as_view(), name='salidas_de_campo_form'),
    # url(r'^(?P<pk>\d+)$', views.Salidas_De_CampoDetailView.as_view(),
    #     name='salidas_de_campo_detail'),
    # url(r'^componente/(?P<pk>\d+)$', views.Componente_Salidas_De_CampoDetailView.as_view(),
    #     name='componente_salidas_de_campo_detail'),
    # url(r'^sensor/(?P<pk>\d+)$', views.Sensor_Salidas_De_CampoDetailView.as_view(),
    #     name='sensor_salidas_de_campo_detail'),
]
