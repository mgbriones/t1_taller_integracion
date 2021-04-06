from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'aplicaciones/home.html')

def contacto(request):
    return render(request,'aplicaciones/contacto.html')