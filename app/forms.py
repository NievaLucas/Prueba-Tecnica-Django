from django import forms
from .models import Transaccion

class FormTransaccion(forms.ModelForm) :

    class Meta :

        model = Transaccion
        fields = [
            'numeroDeCuenta',
            'numeroComprobante',
            'tipoDeComprobante',
            'descripcion',
            'debito',
            'credito'
        ]

        labels = {
            'numeroDeCuenta' : 'Numero de Cuenta',
            'numeroComprobante' : 'Numero de comprobante',
            'tipoDeComprobante' : 'Tipo de comprobante: ',
            'descripcion' : 'Descripcion',
            'debito' : 'Tarjeta de debito',
            'credito' : 'Tarjeta de credito: '
        }

        widgets = {
            'numeroDeCuenta' : forms.TextInput(attrs = {"class" : "form-control", "placeholder" : "Ingrese el numero de cuenta: "}),
            'numeroComprobante' : forms.TextInput(attrs = {"class" : "form-control", "placeholder" : "Ingrese el numero de comprobante: "}),
            'tipoDeComprobante' : forms.TextInput(attrs = {"class" : "form-control", "placeholder" : "Ingrese el tipo de comprobante: "}),
            'descripcion' : forms.TextInput(attrs = {"class" : "form-control", "placeholder" : "(Opcional): "}) ,
            'debito' : forms.NumberInput(attrs = {"class" : "form-control", "placeholder" : "Ingrese monto pagado con tarjeta de debito: "}),
            'credito' : forms.NumberInput(attrs = {"class" : "form-control", "placeholder" : "Ingrese monto pagado con tarjeta de credito: "})
        }