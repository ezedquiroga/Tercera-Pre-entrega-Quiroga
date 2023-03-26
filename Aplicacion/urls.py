from django.urls import path
from Aplicacion.views import guardar_reserva, reserva, huespedes, cancelacion, busqueda_huesped

urlpatterns = [
    path('reserva/', guardar_reserva, name="AplicacionHotelQuiroga"),
    path('reserva/', reserva),
    path('reserva/<nombre>/<habitacion>', reserva),
    path('huespedes/', huespedes, name="AplicacionHuespedes"),
    path('busqueda_huesped/', busqueda_huesped, name="AplicacionBuscarHuesped"),
    path('cancelacion/', cancelacion, name="AplicacionCancelacion")
]