from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def registro(request):
    return render(request, 'login.html')

def registro(request):
    return render(request, 'registro.html')

def libros(request):
    return render(request, 'libros.html')
 
def about(request):
    return render(request, 'about.html') 

def category(request):
    return render(request, 'category.html') 

def contact(request):
    return render(request, 'contact.html') 

def single(request):
    return render(request, 'single.html') 

def single_s(request):
    return render(request, 'single_s.html')

def single_vi(request):
    return render(request, 'single_vi.html')

def styles(request):
    return render(request, 'styles.html')


