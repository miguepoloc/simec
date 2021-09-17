from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from ..api.models import Equipo, Salidas_De_Campo


class FamiliasListView(generic.ListView):
    model = Equipo
    # Cantidadd de items a mostrar por página
    paginate_by = 9
    # El nombre con el que se trabajará en la plantilla html
    context_object_name = 'familias_list'
    queryset = Equipo.objects.order_by('-id')
    # Especifica la localicación del template
    template_name = 'familias/familias_list.html'


class FamiliasDetailView(generic.DetailView):
    model = Equipo
    template_name = 'familias/familias_detail.html'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super().get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        # context['salida_de_campo_list'] = Salidas_De_Campo.objects.filter(sensor=self.kwargs['pk'])
        context['salida_de_campo_list'] = Salidas_De_Campo.objects.all()
        return context
