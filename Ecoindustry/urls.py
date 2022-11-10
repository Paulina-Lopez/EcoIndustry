from django.contrib import admin
from django.urls import path
from appEcoindustry.views import preguntas, agregarBonos, agregarVehiculos, agendaAdmin, comentario, editarBonos, eliminarBonos, inicio, inicioUsuario, bonos, bonosSinUsuario, intercambio, redimir, registro, comentario, agenda, ingresar, administrador, salir, editarUsuario, eliminarUsuario, ingresoIncorrecto, eliminarVehiculo,editarVehiculo, cambiarEstadoAgenda, asignarVehiculo
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administrador/', administrador),
    path('inicio/<nombre>', inicioUsuario),
    path('', inicio),
    path('bonos/<nombre>', bonos),
    path('bonos1/', bonosSinUsuario),
    path('intercambio/', intercambio),
    path('registro/', registro),
    path('comentario/<nombre>', comentario),
    path('agenda/', agenda),
    path('redimir/<nombre>/<int:puntosbono>', redimir),
    path('signin/', ingresar),
    path('signin/<mensaje>', ingresoIncorrecto),
    path('signout/', salir),
    path('editar/', editarUsuario),
    path('editarBonos/', editarBonos),
    path('eliminar/<nombre>', eliminarUsuario),
    path('eliminarBonos/<nombre>', eliminarBonos),
    path('addBonos/', agregarBonos),
    path('verCatalogo/', bonosSinUsuario),
    path('agendaAdmin/', agendaAdmin),
    path('addVehiculos/', agregarVehiculos),
    path('eliminarVehiculo/<placa>', eliminarVehiculo),
    path('editarVehiculo/', editarVehiculo),
    path('ayuda/', preguntas),
    path('cambiarEstadoAgenda/', cambiarEstadoAgenda),
    path('asignarVehiculo/', asignarVehiculo),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
