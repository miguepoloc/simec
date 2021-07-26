from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from ..api.models import *


def Reporte(request):
    return render(request, "reporte/reporte.html")
