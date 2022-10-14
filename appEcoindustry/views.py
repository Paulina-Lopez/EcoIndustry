from django.shortcuts import render, redirect
from .models import Comentario, TipoUsuario, Usuario, Puntos_Usuarios, Bonificacion, Agenda
from django.contrib import messages
from django.contrib.auth import authenticate, login

def iniciop(request, name):
    #empresa = Usuario.objects.all().values()
    #nombreusuario = empresa[0]
    usuario = Usuario.objects.filter(nombreEmpresa = name)
    return render(request, 'index.html', {"name":name,"usuario": usuario})

def inicio(request):
    #empresa = Usuario.objects.all().values()
    #nombreusuario = empresa[0]
    #usuario = Usuario.objects.filter(nombreEmpresa = name)
    return render(request, 'index.html')

def bonos(request, name):
    empresas  = Usuario.objects.all()
    empresaespe = Usuario.objects.filter(nombreEmpresa = name).values()
    print(empresaespe)
    empresaespe = empresaespe[0]
    print(empresaespe)
    puntos = Puntos_Usuarios.objects.filter(identificacion = empresaespe['id']).values()
    print(puntos)
    cantidadp= puntos[0]['cantidad']
    bonificacion=Bonificacion.objects.all()
    return render(request, 'bonos.html', {"name":name, "cantidad": cantidadp, "bono": bonificacion, "empresas": empresas})

def bonos1(request):
    bonificacion=Bonificacion.objects.all()
    return render(request, 'bonos.html', {"bono": bonificacion})


def intercambio(request):
    formulario = request.POST.dict()
    empresa = Usuario.objects.filter(nombreEmpresa = formulario["nombreEmpresa"]).values()
    print(formulario)
    print(empresa)
    id_empresa = empresa[0]
    id_empresa = id_empresa["id"]
    objeto_puntos = Puntos_Usuarios.objects.filter(identificacion = id_empresa).values()
    cantidad_puntos= objeto_puntos[0]
    cantidad_puntos = cantidad_puntos["cantidad"]
    puntos = 0
    if(formulario["tipoMaterial"] == "1"):
        puntos = int(formulario["peso"])*2
    elif(formulario["tipoMaterial"] == "2"):
        puntos = int(formulario["peso"])*3
    elif(formulario["tipoMaterial"] == "3"):
        puntos = int(formulario["peso"])*2
    elif(formulario["tipoMaterial"] == "4"):
        puntos = int(formulario["peso"])*5
    else:
        print("que material es ese?")    
    suma = puntos + cantidad_puntos
    o_p = Puntos_Usuarios.objects.filter(identificacion_id = id_empresa).values()
    o_p.update(cantidad=suma)
    return redirect('/administrador/')

def redimir(request, name, puntosbono):
    usuario=Usuario.objects.filter(nombreEmpresa=name)
    listusuario = usuario.values()
    listusuario = listusuario[0]
    listusuario = listusuario['id']
    objeto_puntos = Puntos_Usuarios.objects.filter(identificacion_id=listusuario).values()
    list_objetos_puntos = objeto_puntos[0]
    cantidad_objetos_puntos = list_objetos_puntos['cantidad']
    if(cantidad_objetos_puntos < puntosbono):
        messages.info(request, 'Your password has been changed successfully!')
        print("no redimió")
        return redirect('/bonos/%s' %(name))
    else:
        o_p = Puntos_Usuarios.objects.filter(identificacion_id=listusuario)
        diferencia = cantidad_objetos_puntos - puntosbono
        o_p.update(cantidad=diferencia)
        print("redimió")
    return redirect('/bonos/%s' %(name))

def registro(request):
    formulario = request.POST.dict()
    T1 = TipoUsuario.objects.get(idtipousuario= request.POST['idtipousuario'])
    empresa = Usuario(nombreEmpresa = formulario['nombreEmpresa'], NIT = formulario['NIT'], direccion = formulario['direccion'], correo = formulario['correo'], clave = formulario['clave'], idtipousuario = T1)
    empresa.save()
    empresa1 = Usuario.objects.filter(nombreEmpresa = formulario['nombreEmpresa']).values()
    empresa1 = empresa1[0]
    puntosU = Puntos_Usuarios(identificacion_id = empresa1['id'], cantidad = 0)
    puntosU.save()
    print(formulario)
    return redirect('/')          

def comentario(request, name):
    formulario = request.POST.dict()
    print(formulario)
    idEmpresa= Usuario.objects.get(nombreEmpresa = request.POST['nombreEmpresa'])   
    comentario = Comentario(identificacion = idEmpresa, desComent = formulario['Comentario'])
    comentario.save()
    return redirect('/inicio/%s' %(name))        

def agenda(request):
    formulario = request.POST.dict()
    print(formulario)
    idEmpresa= Usuario.objects.get(nombreEmpresa = request.POST['nombreEmpresa'])   
    agenda = Agenda(identificacion = idEmpresa, fechaAgenda = formulario['fecha'], estado = 'En proceso')
    agenda.save()
    return redirect('/inicio/%s' %(request.POST['nombreEmpresa']))  

def signin(request):
    formulario=request.POST.dict()
    if request.method == 'POST':
        user = Usuario.objects.filter(nombreEmpresa = formulario["nombreEmpresa"]).filter(clave = formulario["clave"])
        tipouser = user.values()[0]
        print(user.values())
        tipouser = tipouser["idtipousuario_id"]
        
        if len(user.values()) != 0:
            if tipouser == 2:
                return redirect('/administrador/')
            return redirect('/inicio/%s' %(formulario["nombreEmpresa"]))
        else: 
            print("sUPer Malo")
            messages.error(request, "sUPer Malo")
    return render(request, 'login.html')

def signout(request):
    return redirect('/')

#la parte de puntos está en desarrollo, favor no mover 
def administrador(request):
    usuario = Usuario.objects.filter(idtipousuario_id = 1)
    empresas = Usuario.objects.filter(idtipousuario_id = 1).values()
    empresas = list(empresas)
    lista = []
    for empresa in empresas:
        dic_empresa = {}
        dic_empresa["nombre"] = empresa["nombreEmpresa"]
        punto = list(Puntos_Usuarios.objects.filter(identificacion_id = empresa["id"]).values())
        dic_empresa["puntos"] = punto[0]["cantidad"]
        lista.append(dic_empresa)
    return render(request, 'admin.html', {"empresas":usuario, "listapuntos":lista})

def editar(request):
    formulario = request.POST.dict()
    print("editando")
    print(formulario)   
    usuario = Usuario.objects.filter(nombreEmpresa = formulario["nombreEmpresa"])
    idusuario = usuario.values()[0]["id"]
    puntos_usuario = Puntos_Usuarios.objects.filter(identificacion_id = idusuario)
    puntos_usuario.update(cantidad = formulario["puntos"])
    usuario.update(nombreEmpresa = formulario["nombreEmpresa"], NIT = formulario["NIT"], correo = formulario["correo"], clave = formulario["clave"], direccion = formulario["direccion"])
    return redirect("/administrador/")

def eliminar(request, name):
    empresa = Usuario.objects.filter(nombreEmpresa = name)
    empresa.delete()
    return redirect("/administrador/")

def addBonos(request):
    formulario = request.POST.dict()
    print(formulario)
    if request.method == 'POST':
        bonificacion = Bonificacion(nombre = formulario['nombre'], valor = formulario['valor'], imagen = formulario['imagen'])
        bonificacion.save()
    bonos = Bonificacion.objects.all()
    return render(request, 'addBonos.html', {"bonos":bonos})

def eliminarBonos(request, name):
    bono = Bonificacion.objects.filter(nombre = name)
    bono.delete()
    return redirect("/addBonos/")