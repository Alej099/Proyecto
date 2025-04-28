from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

def libros(request):
    return render(request, 'libros.html') 

