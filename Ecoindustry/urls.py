from django.contrib import admin
from django.urls import path
from appEcoindustry.views import addBonos, comentario, eliminarBonos, inicio, iniciop, bonos, bonos1, intercambio, redimir, registro, comentario, agenda, signin, administrador, signout, editar, eliminar
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
    path('comentario/', comentario),
    path('agenda/', agenda),
    path('redimir/<name>/<int:puntosbono>', redimir),
    path('signin/', signin),
    path('signout/', signout),
    path('editar/', editar),
    path('eliminar/<name>', eliminar),
    path('eliminarBonos/<name>', eliminarBonos),
    path('addBonos/', addBonos),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
