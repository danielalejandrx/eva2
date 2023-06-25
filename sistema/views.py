from django.shortcuts import render,redirect
from sistema.forms import FormSeminario
from sistema.models import Inscripcion

# Create your views here.


def index(request):
    lista= Inscripcion.objects.all()
    data= {'verUsuarios':lista}
    return render(request, 'listaDatos.html',data)

def agregarSeminario(request):
    form = FormSeminario()
    if request.method == 'POST':
        form = FormSeminario(request.POST)
        if form.is_valid() :
            nuevaInscripcion = Inscripcion()
            nuevaInscripcion.nombre = form.cleaned_data['nombre']
            nuevaInscripcion.telefono = form.cleaned_data['telefono']
            nuevaInscripcion.fechaSeminario = form.cleaned_data['fechaSeminario']
            nuevaInscripcion.empresaInstitucion = form.cleaned_data['empresaInstitucion']
            nuevaInscripcion.email = form.cleaned_data['email']
            nuevaInscripcion.profesion = form.cleaned_data['profesion']
            nuevaInscripcion.observacion = form.cleaned_data['observacion']
            nuevaInscripcion.save()
        return redirect('/')
    data = {'form' : form}
    return render(request, 'agregarSeminario.html', data)

def modificarSeminario(request, id):
    baseDeDatos = Inscripcion.objects.get(id=id)
    form = FormSeminario(instance=baseDeDatos)

    if request.method == 'POST':
        form = FormSeminario(request.POST, instance=baseDeDatos)
        if form.is_valid():
            form.save()
        return index(request)
    data = {'form': form}
    return render(request, 'agregarSeminario.html', data)


def eliminarSeminario(request, id):
    baseDeDatos = Inscripcion.objects.get(id=id)
    baseDeDatos.delete()
    return redirect('/')

