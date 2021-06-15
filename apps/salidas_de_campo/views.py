from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from ..api.models import *


# class Salidas_De_CampoListView(generic.ListView):
#     model = Salidas_De_Campo
#     # Cantidadd de items a mostrar por página
#     # paginate_by = 5
#     # El nombre con el que se trabajará en la plantilla html
#     context_object_name = 'salida_de_campo_list'
#     # queryset = Salidas_De_Campo.objects.order_by('-id')
#     # Especifica la localicación del template
#     template_name = 'salidas_de_campo/salidas_de_campo_list.html'

#     def get_context_data(self, **kwargs):
#         # Call the base implementation first to get a context
#         context = super().get_context_data(**kwargs)
#         # Add in a QuerySet of all the books
#         context['componentes_salida_de_campo_list'] = Componente_Salidas_De_Campo.objects.all()
#         context['sensores_salida_de_campo_list'] = Sensor_Salidas_De_Campo.objects.all()
#         return context


# class Salidas_De_CampoDetailView(generic.DetailView):
#     model = Salidas_De_Campo
#     context_object_name = 'salidas_de_campo'
#     template_name = 'salidas_de_campo/salidas_de_campo_detail.html'

def Salidas_De_CampoForm(request):

    salidas_de_campo = Salidas_De_Campo.objects.all()
    personal = Personal.objects.all()
    municipio = Municipio.objects.all()
    centro_poblado = Centro_Poblado.objects.all()

    return render(request, "salidas_de_campo/salidas_de_campo_form.html",
                  {'salidas_de_campo': salidas_de_campo, 'personal': personal, 'municipio': municipio, 'centro_poblado': centro_poblado})
