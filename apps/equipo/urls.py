from django.urls import path
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    url(r'^$', views.EquipoListView.as_view(), name='equipo'),
    url(r'^(?P<pk>\d+)$', views.EquipoDetailView.as_view(),
        name='equipo_detail'),
]
