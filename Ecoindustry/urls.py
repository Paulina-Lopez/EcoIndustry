from django.contrib import admin
from django.urls import path
from appEcoindustry.views import comentario, inicio, bonos, intercambio, redimir, registro, comentario, agenda, verCatalogo, ingresar, administrador
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('administrador/', administrador),
    path('', inicio),
    path('bonos/<name>', bonos),
    path('intercambio/', intercambio),
    path('registro/', registro),
    path('comentario/', comentario),
    path('agenda/', agenda),
    path('redimir/<name>/<int:puntosbono>', redimir),
    path('verCatalogo/', verCatalogo),
    path('ingresar/', ingresar),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

