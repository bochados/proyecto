from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import ArtistaForm, PinturaForm
from ObrasArte.models import Artista,Pintura, Obra
# Create your views here.
def listar_pintura(request):
    pintura=Pintura.objects.all()
    return render(request,'lista.html',{'pintura':pintura})

def listar_artista(request):
    artista=Artista.objects.all()
    return render(request,'lista2.html',{'artista':artista})

def Artista_nuevo(request):
    if request.method == "POST":
        formulario = ArtistaForm(request.POST)
        pin = request.POST.getlist('pinturas')
        p = Pintura.objects.all()
        if formulario.is_valid():
            artista=Artista.objects.create(nombre=formulario.cleaned_data['nombre'],edad=formulario.cleaned_data['edad'])
            for pintura_id in request.POST.getlist('pinturas'):
                obras = Obra(pintura_id = pintura_id, artista_id = artista.id)
                obras.save()
            messages.add_message(request, messages.SUCCESS, 'Artista agregada correctamente')
        return redirect('detalle_artista', pk=artista.pk)
    else:
            formulario=ArtistaForm()
    return render (request, 'Artista_editar.html', {'formulario':formulario})

def Pintura_nueva(request):
    if request.method == 'POST':
        formulario =PinturaForm(request.POST)
        if formulario.is_valid():
            pintura=Pintura.objects.create(nombre_pintura=formulario.cleaned_data['nombre_pintura'],estilo=formulario.cleaned_data['estilo'])
            messages.add_message(request, messages.SUCCESS, 'pintura agregada correctamente')
        return redirect('detalle_pintura', pk=pintura.pk)
    else:
        formulario=PinturaForm()
    return render (request, 'Pintura_editar.html', {'formulario':formulario})

def detalle_artista(request, pk):
    post =get_object_or_404(Artista,pk=pk)
    datos = []
    eq=Obra.objects.filter(artista_id=pk)
    for eq in eq:
        nombrepinrtura=Pintura.objects.get(pk=eq.pintura_id)
        datos.append(nombrepinrtura)
    return render(request, 'artistaDetalle.html', {'post':post, 'datos':datos})

def detalle_pintura(request, pk):
        post =get_object_or_404(Pintura,pk=pk)
        return render(request, 'pinturaDetalle.html', {'post':post})

def editar_pintura(request, pk):
    post =get_object_or_404(Pintura, pk=pk)
    if request.method =='POST':
        formulario=PinturaForm(request.POST, instance=post)
        if formulario.is_valid():
            post=formulario.save(commit=false)
            post.save()
            return redirect('/nueva/pintura/', pk=post.id)
    else:
         formulario=PinturaForm(instance=post)
    return render (request,'Pintura_editar.html',{'formulario':formulario})
def eliminar_pintura(request, pk):
    post =get_object_or_404(Pintura, pk=pk)
    post.delete()
    return redirect('listar_pintura')

def eliminar_artista(reques, pk):
    post =get_object_or_404(Artista, pk=pk)
    post.delete()
    return redirect('listar_artista')
