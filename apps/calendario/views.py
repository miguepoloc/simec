from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from ..api.models import Zona, Salidas_De_Campo, Calendario_Salidas_De_Campo, Tipo_Salida_De_Campo, Personal


def calendario(request):

    zona = Zona.objects.all()
    salida = Salidas_De_Campo.objects.all()
    calendario = Calendario_Salidas_De_Campo.objects.all()
    tipo_de_salida = Tipo_Salida_De_Campo.objects.all()

    return render(request, "calendario/calendario.html",
                  {'zona_list': zona, 'salida_de_campo_list': salida, 'calendario_list': calendario, 'tipo_de_salida': tipo_de_salida})
