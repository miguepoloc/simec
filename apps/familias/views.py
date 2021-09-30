from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from ..api.models import *


class FamiliasListView(generic.ListView):
    model = Datos_Vivienda
    # Cantidadd de items a mostrar por página
    paginate_by = 9
    # El nombre con el que se trabajará en la plantilla html
    context_object_name = 'familias_list'
    queryset = Datos_Vivienda.objects.order_by('-nro_ficha')
    # Especifica la localicación del template
    template_name = 'familias/familias_list.html'


# class DatosIntegranteListView(generic.ListView):
#     model = Datos_Integrante
#     # Cantidadd de items a mostrar por página
#     paginate_by = 9
#     # El nombre con el que se trabajará en la plantilla html
#     context_object_name = 'integrante_list'
#     queryset = Datos_Integrante.objects.order_by('-identif')
#     # Especifica la localicación del template
#     template_name = 'familias/integrante_list.html'


class FamiliasDetailView(generic.DetailView):
    model = Datos_Vivienda
    template_name = 'familias/familias_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['datos_integrante_list'] = Datos_Integrante.objects.all()
        return context

class DatosIntegranteDetailView(generic.DetailView):
    model = Datos_Integrante
    template_name = 'familias/datos_integrante_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context['datos_integrante_list'] = Datos_Integrante.objects.all()
        return context