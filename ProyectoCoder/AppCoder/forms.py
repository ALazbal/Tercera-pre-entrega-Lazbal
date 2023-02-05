from django import forms

class CursoFormulario(forms.Form):

    nombre = forms.CharField()
    camada = forms.IntegerField()


class EntregableFormulario(forms.Form):

    nombre = forms.CharField()
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField()

class ProfesoresFormulario(forms.Form):

    nombre = forms.CharField()
    apellido = forms.CharField()
    email = forms.EmailField()
    profesion = forms.CharField()
    # agregamos un dato - se hace un nueva migracion
    edad = forms.IntegerField() # numero por defecto, sino no toma la columna    

class EstudiantesFormulario(forms.Form):

    # no se pone __init__ se ingresan atributos directo

    nombre = forms.CharField()
    apellido = forms.CharField()
    camada = forms.IntegerField()
     