from django.contrib import admin
from django.urls import path
from appEcoindustry.views import addBonos, addVehiculos, agendaAdmin, comentario, editarBonos, eliminarBonos, inicio, iniciop, bonos, bonos1, intercambio, redimir, registro, comentario, agenda, signin, administrador, signout, editar, eliminar, signinMalo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administrador/', administrador),
    path('inicio/<name>', iniciop),
    path('', inicio),
    path('bonos/<name>', bonos),
    path('bonos1/', bonos1),
    path('intercambio/', intercambio),
    path('registro/', registro),
    path('comentario/<name>', comentario),
    path('agenda/', agenda),
    path('redimir/<name>/<int:puntosbono>', redimir),
    path('signin/', signin),
    path('signin/<mensaje>', signinMalo),
    path('signout/', signout),
    path('editar/', editar),
    path('editarBonos/', editarBonos),
    path('eliminar/<name>', eliminar),
    path('eliminarBonos/<name>', eliminarBonos),
    path('addBonos/', addBonos),
    path('agendaAdmin/', agendaAdmin),
    path('addVehiculos/', addVehiculos),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
