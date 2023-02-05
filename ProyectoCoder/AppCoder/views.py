from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.models import * 
from AppCoder.forms import *

def inicio(request):

    return render(request, "AppCoder/inicio.html")



def ver_estudiantes(request):

    listaEstudiantes = Estudiante.objects.all()

    return render(request, "AppCoder/verEstudiantes.html", {"listaEstudiantes":listaEstudiantes})
    

def ver_profesores(request):

    listaProfes = Profesor.objects.all()

    return render(request, "AppCoder/verProfesores.html", {"listaProfes":listaProfes})

def ver_entregables(request):

    listaEntregables = Entregable.objects.all()

    return render(request, "AppCoder/verEntregables.html", {"listaEntregables":listaEntregables})


def ver_curso(request):

    listaCursos = Curso.objects.all()

    return render(request, "AppCoder/verCursos.html", {"listaCursos":listaCursos})               



#-------------------- FORMULARIOS ------------------------------------

def cursoFormulario(request): # FORM CON DJANGO

    if request.method == 'POST':

        formulario1 = CursoFormulario(request.POST)
        
        print(formulario1)

        if formulario1.is_valid(): #validar que los datos esten bien

            info = formulario1.cleaned_data 

            print(info)

            curso = Curso(nombre = info["nombre"], camada = info["camada"])

            curso.save()

            return render(request, "AppCoder/inicio.html") 
    
    else:

        formulario1 = CursoFormulario()

    return render(request, "AppCoder/cursoFormulario.html",{"formulario":formulario1})    


def profesoresFormulario(request):

    if request.method == 'POST':

        formulario1 = ProfesoresFormulario(request.POST)


        if formulario1.is_valid(): #validar que los datos esten bien

            info = formulario1.cleaned_data 

            profesor1 = Profesor(nombre = info["nombre"], apellido = info["apellido"],
            email = info["email"], profesion = info["profesion"], edad = info["edad"])

            profesor1.save()

            return render(request, "AppCoder/inicio.html") 
    
    else:

        formulario1 = ProfesoresFormulario()

    return render(request, "AppCoder/profesoresFormulario.html",{"formulario":formulario1}) 


def estudiantesFormulario(request):

    if request.method == 'POST':

        formulario1 = EstudiantesFormulario(request.POST)


        if formulario1.is_valid(): #validar que los datos esten bien

            info = formulario1.cleaned_data 

            estudiante1 = Estudiante(nombre = info["nombre"], apellido = info["apellido"],
            camada = info["camada"])

            estudiante1.save()

            return render(request, "AppCoder/inicio.html") 
    
    else:

        formulario1 = EstudiantesFormulario()

    return render(request, "AppCoder/estudiantesFormulario.html",{"formulario":formulario1}) 


def entregablesFormulario(request):

    if request.method == 'POST':

        formulario1 = EntregableFormulario(request.POST)


        if formulario1.is_valid(): #validar que los datos esten bien

            info = formulario1.cleaned_data 

            entregable1 = Entregable(nombre = info["nombre"], fechaDeEntrega = info["fechaDeEntrega"],
            entregado = info["entregado"])

            entregable1.save()

            return render(request, "AppCoder/inicio.html") 
    
    else:

        formulario1 = EntregableFormulario()

    return render(request, "AppCoder/entregablesFormulario.html",{"formulario":formulario1}) 

#----------------- BUSQUEDA DE DATOS-------------------------------

def busquedaCamada(request):

    return render(request, "AppCoder/busquedaCamada.html")


def resultadoBusqueda(request):

    if request.method == "GET":

        camada = request.GET["camada"]
        cursosResultado = Curso.objects.filter(camada__icontains = camada)

        return render(request, "AppCoder/resultadosBusqueda.html",{"camada":camada, "resultado": cursosResultado})

    return render(request,"AppCoder/resultadosBusqueda.html")   