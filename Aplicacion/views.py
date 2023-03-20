from django.shortcuts import render
from Aplicacion.models import Reserva
# Create your views here.
def guardar_reserva(request):
    reserva = Reserva()
    reserva.save()
    return render(request, "base.html")

def reserva(request):
    all_reservas = Reserva.objects.all()
    context = {
        "reservas" : all_reservas
    }
    return render(request, "Aplicacion/reserva.html", context=context)

def crear_reserva(request, nombre, habitacion):
    save_reserva = Reserva(nombre=nombre, habitacion=habitacion)
    save_reserva.save()
    context = {
        "nombre": nombre
    }
    return render(request, "Aplicacion/crear_reserva.html", context)

def huespedes(request):
    return render(request, "Aplicacion/huespedes.html")

def cancelacion(request):
    return render(request, "Aplicacion/cancelacion.html")