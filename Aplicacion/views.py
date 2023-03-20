from django.shortcuts import render
from Aplicacion.models import Reserva
from django.http import HttpResponse
# Create your views here.
def guardar_reserva(request):
    reserva = Reserva()
    reserva.save()
    return HttpResponse("Se ha reservado su habitacion")