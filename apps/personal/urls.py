from django.urls import path
from django.conf.urls import url
from django.urls import path, include
from rest_framework import routers
from . import views

urlpatterns = [
    url(r'^$', views.PersonalListView.as_view(), name='personal'),
    url(r'^(?P<pk>\d+)$', views.PersonalDetailView.as_view(),
        name='personal_detail'),
]
