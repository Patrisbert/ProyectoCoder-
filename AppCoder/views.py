from django.shortcuts import render
from AppCoder.models import Curso
from django.http import HttpResponse
from AppCoder.forms import CursoFormulario

# Create your views here.

def curso(self):
    curso=Curso(nombre="Desarrollo Web", camada=12345)
    curso.save()

    documentoDeTexto = f'---> Curso: {curso.nombre} Camada: {curso.camada}'
    return HttpResponse(documentoDeTexto)

def inicio(request):
    return render(request, 'inicio.html')

# def cursos(request):
#  return render(request, 'cursos.html')

def profesores(request):
    return render(request, 'profesores.html')

def estudiantes(request):
    return render(request, 'estudiantes.html')

def entregables(request):
    return render(request, 'entregables.html')

def cursos(request):
    if request.method == 'POST':
        miFormulario = CursoFormulario(request.POST)

        print(miFormulario)

        if miFormulario.is_valid:
            
            informacion = miFormulario.cleaned_data

            curso = Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            curso.save()
            return render(request, 'inicio.html')
    else:
        miFormulario = CursoFormulario()
         
    return render(request, 'cursos.html', {'miFormulario':miFormulario})

def busquedaCamada(request):
    return render(request, 'busquedaCamada.html')

def buscar(request):
    if request.GET['camada']:
        camada = request.GET['camada']
        curso = Curso.objects.filter(camada__icontains=camada)
        
        return render(request, 'inicio.html', {'cursos':curso, 'camada':camada})
    else:
        respuesta = f"No se han enviado datos."

    # return HttpResponse(respuesta)
    return render(request, 'inicio.html', {"respuesta":respuesta})

