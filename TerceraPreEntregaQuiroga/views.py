import datetime
from django.http import HttpResponse
from django.shortcuts import render


def saludo(request):
    return HttpResponse("Hola")

def segunda_vista(request):
    return HttpResponse("<br><br>Segundo saludo")

def diaDeHoy(request):

    dia = datetime.datetime.now()

    documentoDeTexto = f"Hoy es dia: <br> {dia}"

    return HttpResponse(documentoDeTexto)

def show_html(request):
    return render(request, "template1.html")

def show_html2(request, reserva):
    contexto ={
        "reserva": reserva,
        "nombre": "Hotel Quiroga",
    }
    return render(request, "template2.html", context=contexto)


