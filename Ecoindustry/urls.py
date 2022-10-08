<<<<<<< HEAD
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
=======
"""Ecoindustry URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from appEcoindustry.views import inicio, bonos, intercambio, redimir

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/', inicio),
    path('bonos/<name>', bonos),
    path('intercambio/<name>', intercambio),
    path('redimir/<name>/<int:puntosbono>', redimir),
]
>>>>>>> origin
