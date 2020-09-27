from django.urls import path
from .views import Consultarusuarios, ReporteUsuarios, ConsultarEstadosDB, ReporteEstadosDB, ConsultarUltimoBck
from .views import ReporteUltimosBck, EjecucionJobBck, ReporteEjecucionJobBck, GenArchivosBak, ReporteArchivosBak, CumplimientoBck
from .views import ReporteCumplimientoBck

urlpatterns = [
    path('usuarios_registrados/', Consultarusuarios, name='usuarios_registrados'),
    path('reporte_usuarios/', ReporteUsuarios.as_view(), name='reporte_usuarios'),
    path('estado_db/', ConsultarEstadosDB, name='estado_db'),
    path('reporte_db/', ReporteEstadosDB.as_view(), name='reporte_db'),
    path('ultimos_bck/', ConsultarUltimoBck, name='ultimos_bck_db'),
    path('reporte_ultimobck/', ReporteUltimosBck.as_view(), name='reporte_ultimobck'),
    path('jobs_bck/', EjecucionJobBck, name='jobs_bck'),
    path('reporte_jobsbck/', ReporteEjecucionJobBck.as_view(), name='reporte_jobsbck'),
    path('archivos_bak/', GenArchivosBak, name='archivos_bak'),
    path('reporte_genBak/', ReporteArchivosBak.as_view(), name='reporte_genBak'),
    path('cumplimiento_bck/', CumplimientoBck, name='cumplimiento_bck'),
    path('reporte_cumplimiento/', ReporteCumplimientoBck.as_view(), name='reporte_cumplimiento'),
]