from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from ..api.models import Equipo, Zona, Personal, Salidas_De_Campo, Calendario_Salidas_De_Campo, Equipo


def index(request):

    zona = Zona.objects.all()
    personal = Personal.objects.all()
    equipo = Equipo.objects.all()
    salida = Salidas_De_Campo.objects.all()
    calendario = Calendario_Salidas_De_Campo.objects.all()

    return render(request, "main/index.html", {'zona_list': zona, 'personal_list': personal, 'equipo_list': equipo, 
        'salida_de_campo_list': salida, 'calendario_list': calendario})
