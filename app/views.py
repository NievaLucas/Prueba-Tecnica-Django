from django.http.response import JsonResponse
from django.shortcuts import render, redirect
from django.views import View
from .forms import FormTransaccion
from .models import Transaccion

# Create your views here.
 
def jsonAccount(self, _request) :
    historialTransacciones = list(Transaccion.objects.values())
    return JsonResponse({'historialTransacciones' : historialTransacciones})

# Vista a DataTables
class Account(View) :
    def get(self, request) :
        return render(request, 'accounts.html')

template_name = "sendTransaccion.html"

# Vista y funcionamiento de subida de Transacciones
class SendTransaccion(View) :

    formClass = FormTransaccion()
    
    def get(self, request, *args, **kwargs) : 
        return render(request, template_name, {'form' : self.formClass})
    
    def post(self, request, *args, **kwargs) :
        form = FormTransaccion(request.POST)

        if form.is_valid() :
            form.save()
            return redirect('accounts')
        
        return render(request, template_name, {'form' : self.formClass})
    
# Vista al UPDATE de las transferencias
class UpdateTransaccion(View) :

    def get(self, request, id, *args, **kwargs) :
        value = Transaccion.objects.get(pk = id)
        form = FormTransaccion(instance = value)
        return render(request, template_name, {'form' : form})

    def post(self, request, id, *arg, **kwargs) :
       
        instance = Transaccion.objects.get(pk = id)
        form = FormTransaccion(request.POST, instance = instance)

        if form.is_valid() :
            form.save()
            return redirect('accounts')
        
        return render(request, template_name, {'form' : form})