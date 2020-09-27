from django.contrib import admin
from .models import Instancias,TipoBckls,BasesDatos,PoliticasBck,Periodicidad, Programacionbck

admin.site.register(PoliticasBck)
admin.site.register(Instancias)
admin.site.register(BasesDatos)
admin.site.register(TipoBckls)
admin.site.register(Periodicidad)
admin.site.register(Programacionbck)
