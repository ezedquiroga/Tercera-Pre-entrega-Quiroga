from django.shortcuts import render
from Aplicacion.models import Reserva, Huespedes, Cancelacion
from Aplicacion.forms import HuespedesForm, CancelacionForm, ReservaForm, BusquedaHuespedForm
# Create your views here.
def guardar_reserva(request):
    reserva = Reserva()
    reserva.save()
    return render(request, "base.html")

def reserva(request):
    all_reservas = Reserva.objects.all()
    if request.method == "POST":
        mi_formulario3 = ReservaForm(request.POST)

        if mi_formulario3.is_valid():
            informacion = mi_formulario3.cleaned_data
            reserva_save = Reserva(
                nombre=informacion['nombre'],
                habitacion=informacion['habitacion'],
                fecha=informacion['fecha']
            )
            reserva_save.save()
    context = {
        "reservas": all_reservas,
        "form": ReservaForm()
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

    if request.method == "POST":
        mi_formulario = HuespedesForm(request.POST)

        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            huespedes_save = Huespedes(
                nombre=informacion['nombre'],
                email=informacion['email'],
                telefono=informacion['telefono']
            )
            huespedes_save.save()

    context = {
        "form": HuespedesForm(),
        "form_busqueda": BusquedaHuespedForm()
    }
    return render(request, "Aplicacion/huespedes.html", context=context)

def cancelacion(request):

    if request.method == "POST":
        mi_formulario2 = CancelacionForm(request.POST)

        if mi_formulario2.is_valid():
            informacion = mi_formulario2.cleaned_data
            cancelacion_save = Cancelacion(
                nombre=informacion['nombre'],
            )
            cancelacion_save.save()

    context = {
        "form": CancelacionForm()
    }
    return render(request, "Aplicacion/cancelacion.html", context=context)

def busqueda_huesped(request):

    mi_formulario4 = BusquedaHuespedForm(request.GET)
    if mi_formulario4.is_valid():
        informacion = mi_formulario4.cleaned_data
        huespedes_buscados = Huespedes.objects.filter(nombre__icontains=informacion['nombre'])
        context = {
            "huespedes": huespedes_buscados
        }
        return render(request, "Aplicacion/busqueda_huesped.html", context=context)