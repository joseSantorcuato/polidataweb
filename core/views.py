from django.shortcuts import render

def patrones(request):
    return render(request, 'patrones.html')

def home(request):
    return render(request, 'home.html')

def evaluacion(request):
    return render(request, 'evaluacion.html')


def sistemas (request):
    return render(request, 'sistemas.html')


def aprendizaje(request):
    return render(request, 'aprendizaje.html')