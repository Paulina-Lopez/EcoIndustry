from django.shortcuts import render

def inicio(request):
    return render(request, 'index.html')

def bonos(request):
    return render(request, 'bonos.html')