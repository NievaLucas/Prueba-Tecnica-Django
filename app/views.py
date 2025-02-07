from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms import formTransaccion
from .models import Transaccion

# Create your views here.

def accounts(request) :

    return render(request, 'accounts.html')

def accountsTransaccion(_request) :
        
    historialTransacciones = list(Transaccion.objects.values())
    date = {'historialTransacciones' : historialTransacciones}
    return JsonResponse(date)

def sendTransaccion(request) :

    if request.method == 'POST' :
        form = formTransaccion(request.POST)
        if form.is_valid() :

            # Guardamos en la Base de Datos
            form.save()

            return redirect('accounts')
    else :
        form = formTransaccion()
    return render(request, 'sendTransaccion.html', {'form' : form})
    
