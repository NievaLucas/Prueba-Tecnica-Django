from django.db import models

# Create your models here.

class Transaccion(models.Model) :

    numeroDeCuenta = models.IntegerField(unique = True, blank = False)
    numeroComprobante = models.CharField(max_length = 20, blank = False)
    tipoDeComprobante = models.CharField(max_length = 20, blank = False)
    descripcion = models.CharField(max_length = 1000, blank = True)
    debito = models.DecimalField(max_digits = 10, decimal_places = 2, blank = False)
    credito = models.DecimalField(max_digits = 10, decimal_places = 2, blank = False)
    