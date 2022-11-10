from django.shortcuts import render, redirect
from .models import Comentario, TipoUsuario, Usuario, Puntos_Usuarios, Bonificacion, Agenda, Vehiculo
from django.contrib import messages
from django.contrib.auth import authenticate, login


def inicioUsuario(request, nombre):
    usuario = Usuario.objects.filter(nombreEmpresa=nombre)
    return render(request, 'index.html', {"name": nombre, "usuario": usuario})


def inicio(request):
    return render(request, 'index.html')

def preguntas(request):
    return render(request, 'preguntas_frec.html')

def bonos(request, nombre):
    empresas = Usuario.objects.all()
    empresaespe = Usuario.objects.filter(nombreEmpresa=nombre).values()
    print(empresaespe)
    empresaespe = empresaespe[0]
    print(empresaespe)
    puntos = Puntos_Usuarios.objects.filter(
        identificacion=empresaespe['id']).values()
    print(puntos)
    cantidadp = puntos[0]['cantidad']
    bonificacion = Bonificacion.objects.all()
    return render(request, 'bonos.html', {"name": nombre, "cantidad": cantidadp, "bono": bonificacion, "empresas": empresas})


def bonosSinUsuario(request):
    bonificacion = Bonificacion.objects.all()
    return render(request, 'bonos.html', {"bono": bonificacion})


def intercambio(request):
    formulario = request.POST.dict()
    empresa = Usuario.objects.filter(
        nombreEmpresa=formulario["nombreEmpresa"]).values()
    print(formulario)
    print(empresa)
    id_empresa = empresa[0]
    id_empresa = id_empresa["id"]
    objeto_puntos = Puntos_Usuarios.objects.filter(
        identificacion=id_empresa).values()
    cantidad_puntos = objeto_puntos[0]
    cantidad_puntos = cantidad_puntos["cantidad"]
    puntos = 0
    if (formulario["tipoMaterial"] == "1"):
        puntos = int(formulario["peso"])*2
    elif (formulario["tipoMaterial"] == "2"):
        puntos = int(formulario["peso"])*3
    elif (formulario["tipoMaterial"] == "3"):
        puntos = int(formulario["peso"])*2
    elif (formulario["tipoMaterial"] == "4"):
        puntos = int(formulario["peso"])*5
    else:
        print("que material es ese?")
    suma = puntos + cantidad_puntos
    o_p = Puntos_Usuarios.objects.filter(identificacion_id=id_empresa).values()
    o_p.update(cantidad=suma)
    return redirect('/administrador/')


def redimir(request, nombre, puntosbono):
    usuario = Usuario.objects.filter(nombreEmpresa=nombre)
    listusuario = usuario.values()
    listusuario = listusuario[0]
    listusuario = listusuario['id']
    objeto_puntos = Puntos_Usuarios.objects.filter(
        identificacion_id=listusuario).values()
    list_objetos_puntos = objeto_puntos[0]
    cantidad_objetos_puntos = list_objetos_puntos['cantidad']
    if (cantidad_objetos_puntos < puntosbono):
        messages.info(request, 'Your password has been changed successfully!')
        print("no redimió")
        return redirect('/bonos/%s' % (nombre))
    else:
        o_p = Puntos_Usuarios.objects.filter(identificacion_id=listusuario)
        diferencia = cantidad_objetos_puntos - puntosbono
        o_p.update(cantidad=diferencia)
        print("redimió")
    return redirect('/bonos/%s' % (nombre))


def registro(request):
    formulario = request.POST.dict()
    T1 = TipoUsuario.objects.get(idtipousuario=request.POST['idtipousuario'])
    empresa = Usuario(nombreEmpresa=formulario['nombreEmpresa'], NIT=formulario['NIT'],
                      direccion=formulario['direccion'], correo=formulario['correo'], clave=formulario['clave'], idtipousuario=T1)
    empresa.save()
    empresa1 = Usuario.objects.filter(
        nombreEmpresa=formulario['nombreEmpresa']).values()
    empresa1 = empresa1[0]
    puntosU = Puntos_Usuarios(identificacion_id=empresa1['id'], cantidad=0)
    puntosU.save()
    print(formulario)
    return redirect('/')


def comentario(request, nombre):
    formulario = request.POST.dict()
    print(formulario)
    idEmpresa = Usuario.objects.get(
        nombreEmpresa=request.POST['nombreEmpresa'])
    comentario = Comentario(identificacion=idEmpresa,
                            desComent=formulario['Comentario'])
    comentario.save()
    return redirect('/inicio/%s' % (nombre))


def agenda(request):
    formulario = request.POST.dict()
    print(formulario)
    idEmpresa = Usuario.objects.get(
        nombreEmpresa=request.POST['nombreEmpresa'])
    agenda = Agenda(identificacion=idEmpresa,
                    fechaAgenda=formulario['fecha'], estado='En proceso')
    agenda.save()
    return redirect('/inicio/%s' % (request.POST['nombreEmpresa']))


def ingresar(request):
    formulario = request.POST.dict()
    if request.method == 'POST':
        try:
            user = Usuario.objects.filter(
                nombreEmpresa=formulario["nombreEmpresa"]).filter(clave=formulario["clave"])
            tipouser = user.values()[0]
            print(user.values())
            tipouser = tipouser["idtipousuario_id"]
            if tipouser == 2:
                return redirect('/administrador/')
            return redirect('/inicio/%s' % (formulario["nombreEmpresa"]))
        except:
            return redirect('/signin/%s' % ("error"))
    return render(request, 'login.html')


def ingresoIncorrecto(request, mensaje):
    formulario = request.POST.dict()
    if request.method == 'POST':
        try:
            user = Usuario.objects.filter(
                nombreEmpresa=formulario["nombreEmpresa"]).filter(clave=formulario["clave"])
            tipouser = user.values()[0]
            print(user.values())
            tipouser = tipouser["idtipousuario_id"]
            if tipouser == 2:
                return redirect('/administrador/')
            return redirect('/inicio/%s' % (formulario["nombreEmpresa"]))
        except:
            return redirect('/signin/%s' % ("error"))
    return render(request, 'login.html', {"alerta": mensaje})

def salir(request):
    return redirect('/')

def administrador(request):
    usuario = Usuario.objects.filter(idtipousuario_id=1)
    empresas = Usuario.objects.filter(idtipousuario_id=1).values()
    empresas = list(empresas)
    lista = []
    for empresa in empresas:
        dic_empresa = {}
        dic_empresa["nombre"] = empresa["nombreEmpresa"]
        punto = list(Puntos_Usuarios.objects.filter(
            identificacion_id=empresa["id"]).values())
        dic_empresa["puntos"] = punto[0]["cantidad"]
        lista.append(dic_empresa)
    return render(request, 'admin.html', {"empresas": usuario, "listapuntos": lista})


def editarUsuario(request):
    formulario = request.POST.dict()
    print("editando")
    print(formulario)
    usuario = Usuario.objects.filter(nombreEmpresa=formulario["nombreEmpresa"])
    idusuario = usuario.values()[0]["id"]
    puntos_usuario = Puntos_Usuarios.objects.filter(identificacion_id=idusuario)
    puntos_usuario.update(cantidad=formulario["puntos"])
    usuario.update(nombreEmpresa=formulario["nombreEmpresa"], NIT=formulario["NIT"],
                   correo=formulario["correo"], clave=formulario["clave"], direccion=formulario["direccion"])
    return redirect("/administrador/")


def editarBonos(request):
    formulario = request.POST.dict()
    print("editando")
    print(formulario)
    bonificacion = Bonificacion.objects.filter(nombre=formulario["nombre"])
    bonificacion.update(
        nombre=formulario["nombre"], valor=formulario["valor"], imagen=formulario["imagen"])
    return redirect("/addBonos/")


def eliminarUsuario(request, nombre):
    empresa = Usuario.objects.filter(nombreEmpresa=nombre)
    empresa.delete()
    return redirect("/administrador/")


def agregarBonos(request):
    formulario = request.POST.dict()
    print(formulario)
    if request.method == 'POST':
        bonificacion = Bonificacion(
            nombre=formulario['nombre'], valor=formulario['valor'], imagen=formulario['imagen'])
        bonificacion.save()
    bonos = Bonificacion.objects.all()
    return render(request, 'addBonos.html', {"bonos": bonos})


def eliminarBonos(request, nombre):
    bono = Bonificacion.objects.filter(nombre=nombre)
    bono.delete()
    return redirect("/addBonos/")


def agendaAdmin(request):
    vehiculos = Vehiculo.objects.all()
    agendas = Agenda.objects.all()
    empresa = Usuario.objects.filter(idtipousuario_id=1)
    return render(request, 'agenda.html',  {"agendas": agendas, "vehiculos": vehiculos, "empresas":empresa})

def cambiarEstadoAgenda(request):
    formulario = request.POST.dict()
    print(formulario)
    agenda = Agenda.objects.filter(idAgenda = formulario["idAgenda"])
    agenda.update(estado = formulario["estado"])
    return redirect("/agendaAdmin/")

def asignarVehiculo(request):
    formulario = request.POST.dict()
    print(formulario)
    agenda = Agenda.objects.filter(idAgenda = formulario["idAgenda"])
    agenda.update(placa = formulario["placa"])
    return redirect("/agendaAdmin/")

def agregarVehiculos(request):
    formulario = request.POST.dict()
    print(formulario)
    if request.method == 'POST':
        vehiculo = Vehiculo(nombreConductor=formulario['nombreConductor'], placa=formulario['placa'],
                            capacidad=formulario['capacidad'], disponibilidad=formulario['disponibilidad'])
    vehiculo.save()
    return redirect("/agendaAdmin/")

def editarVehiculo(request):
    formulario = request.POST.dict()
    print("editando")
    print(formulario)
    vehiculo = Vehiculo.objects.filter(placa=formulario["placa"])
    vehiculo.update(
        placa=formulario["placa"], nombreConductor=formulario["nombreConductor"], capacidad=formulario["capacidad"], disponibilidad=formulario["disponibilidad"])
    return redirect("/agendaAdmin/")

def eliminarVehiculo(request, placa):
    vehiculo = Vehiculo.objects.filter(placa=placa)
    try: 
        agenda = Agenda.objects.filter(placa = placa).filter(estado = "En proceso")
        agenda.update(placa = " ")
    except:
        print("no hay agendas de este tipo")
    vehiculo.delete()
    return redirect("/agendaAdmin/")