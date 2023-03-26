from django import forms


class ReservaForm(forms.Form):

    nombre = forms.CharField(max_length=40)
    habitacion = forms.CharField(max_length=40)
    fecha = forms.CharField(max_length=10)
class HuespedesForm(forms.Form):

    nombre = forms.CharField(max_length=40)
    email = forms.CharField(max_length=40)
    telefono = forms.IntegerField()


class CancelacionForm(forms.Form):

    nombre = forms.CharField(max_length=40)


class BusquedaHuespedForm(forms.Form):

    nombre = forms.CharField(max_length=40)