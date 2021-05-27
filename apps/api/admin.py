from django.contrib import admin
from .models import (Zona, Tipo_Salida_De_Campo, Personal, Salidas_De_Campo, Calendario_Salidas_De_Campo)

admin.site.register(Zona)
admin.site.register(Tipo_Salida_De_Campo)
admin.site.register(Salidas_De_Campo)
admin.site.register(Personal)
admin.site.register(Calendario_Salidas_De_Campo)
