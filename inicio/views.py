from django.shortcuts import render

def inicio (request):
    return render (request, 'inicio/inicio.html')


def nosotros (request):
    return render (request , 'inicio/nosotros.html')

