from django.urls import path
from AppCoder.views import *


urlpatterns = [ 
    
    path("inicio/", inicio, name= "Inicio"),
    path("ver_estudiantes/", ver_estudiantes, name="Ver Estudiantes"),
    path("ver_profesores/", ver_profesores, name="Ver Profesores"),
    path("ver_entregables/", ver_entregables, name="Ver Entregables"),
    path("ver_curso/", ver_curso, name="Ver Cursos"),
    
    #buscar informacion
    path("buscar_camada/", busquedaCamada, name="Buscar Camada"),
    path("resultados_busqueda/", resultadoBusqueda, name="Resultado Busqueda"),

    #formularios
    path("crear_curso/", cursoFormulario, name="Crear Curso"),
    path("crear_profesor/", profesoresFormulario, name="Crear Profesor"),
    path("crear_estudiante/", estudiantesFormulario, name="Crear Estudiante"),
    path("crear_entregables/", entregablesFormulario, name= "Crear Entregable")
   
   ]