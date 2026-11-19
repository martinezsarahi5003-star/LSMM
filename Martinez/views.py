from django.shortcuts import render

def inicio (request):
    return render (request, 'Martinez/inicio.html')
def registro(request):
    return render (request, 'Martinez/formregistro.html' )