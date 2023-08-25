from django.shortcuts import render
from .models import Remate, Licitacion, Martillero, Cliente, Operador
from django.http import HttpResponse
from .forms import licitacionForm, clienteForm, martilleroForm, operadorForm, remateForm

# Creo las vistas.

def inicio(request):
    return render(request, 'inicio.html')

# Vistas de los elementos

def remates(request):
    if request.method=='POST':
        form=remateForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            bien=info['bien']
            base=info['base']
            fecha=info['fecha']
            lugar=info['lugar']
            remate=Remate(bien=bien,base=base,fecha=fecha,lugar=lugar)
            remate.save()
            mensaje='Remate creado'
            
        else:
            mensaje='Datos inválidos'
        remates=Remate.objects.all()
        remate_formulario=remateForm()
        return render(request,'remates.html', {'mensaje':mensaje, 'formulario':remate_formulario, 'remates':remates})
    
    else:
        remate_formulario=remateForm()
        remates=Remate.objects.all()
    
    return render(request,'remates.html', {'formulario':remate_formulario, 'remates':remates})

def licitaciones(request):
    if request.method=='POST':
        form=licitacionForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            objeto=info['objeto']
            referencia=info['referencia']
            fecha=info['fecha']
            link=info['link']
            licitacion=Licitacion(objeto=objeto,referencia=referencia,fecha=fecha,link=link)
            licitacion.save()
            mensaje='Licitación creada'
            
        else:
            mensaje='Datos inválidos'
        licitacion=Licitacion.objects.all()
        licitacion_formulario=licitacionForm()
        return render(request,'licitacion.html', {'mensaje':mensaje, 'formulario':licitacion_formulario, 'licitaciones':licitaciones})
    
    else:
        licitacion_formulario=licitacionForm()
        licitacion=Licitacion.objects.all()
    
    return render(request,'licitaciones.html', {'formulario':licitacion_formulario, 'licitaciones':licitaciones})
    
def martilleros(request):
    if request.method=='POST':
        form=martilleroForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info['nombre']
            apellido=info['apellido']
            matricula=info['matricula']
            email=info['email']
            martillero=Martillero(nombre=nombre,apellido=apellido,matricula=matricula,email=email)
            martillero.save()
            mensaje='Martillero creado'
            
        else:
            mensaje='Datos inválidos'
        martillero=Martillero.objects.all()
        martillero_formulario=martilleroForm()
        return render(request,'martilleros.html', {'mensaje':mensaje, 'formulario':martillero_formulario, 'martilleros':martilleros})
    
    else:
        martillero_formulario=martilleroForm()
        martillero=Martillero.objects.all()
    
    return render(request,'martilleros.html', {'formulario':martillero_formulario, 'martilleros':martilleros})

def clientes(request):
    if request.method=='POST':
        form=clienteForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info['nombre']
            apellido=info['apellido']
            numero_de_cliente=info['numero_de_cliente']
            email=info['email']
            cliente=Cliente(nombre=nombre,apellido=apellido,numero_de_cliente=numero_de_cliente,email=email)
            cliente.save()
            cliente_formulario=clienteForm()
            return render(request,'clientes.html', {'mensaje':'Cliente cargado', 'formulario':cliente_formulario})
        return render(request,'clientes.html', {'mensaje':'Datos inválidos'})
    else:
        cliente_formulario=clienteForm()
        return render(request,'clientes.html', {'formulario':cliente_formulario})
    
    
def operadores(request):
    if request.method=='POST':
        form=operadorForm(request.POST)
        if form.is_valid():
            info=form.cleaned_data
            nombre=info['nombre']
            apellido=info['apellido']
            email=info['email']
            operador=Operador(nombre=nombre,apellido=apellido,email=email)
            operador.save()
            operador_formulario=operadorForm()
            return render(request,'operadores.html', {'mensaje':'Operador cargado', 'formulario':operador_formulario})
        return render(request,'operadores.html', {'mensaje':'Datos inválidos'})
    else:
        operador_formulario=operadorForm()
        return render(request,'operadores.html', {'formulario':operador_formulario})  

# Vista de búsquedas y resultados

# Remates

def busquedaRemate(request):
    return render(request,'busqueda_remates.html')

def busquedaBien(request):
    bien=request.GET['bien']
    if bien!='':
        remates=Remate.objects.filter(bien__icontains=bien)
        return render(request,'resultados_remates.html', {'remates':remates})
    else:
        return render(request,'busqueda_remates.html', {'mensaje':'Por favor, ingresá algún término de búsqueda'})

# Licitaciones 

def busquedaLicitacion(request):
    return render(request,'busqueda_licitaciones.html')

def busquedaObjeto(request):
    objeto=request.GET['objeto']
    if objeto!='':
        licitaciones=Licitacion.objects.filter(objeto__icontains=objeto)
        return render(request,'resultados_licitaciones.html', {'licitaciones':licitaciones})
    else:
        return render(request,'busqueda_licitaciones.html', {'mensaje':'Por favor, ingresá algún término de búsqueda'})
    
# Clientes 

def busquedaCliente(request):
    return render(request,'busqueda_clientes.html')

def busquedaNumero(request):
    numero_de_cliente=request.GET['numero_de_cliente']
    if numero_de_cliente!='':
        clientes=Cliente.objects.filter(numero_de_cliente__icontains=numero_de_cliente)
        return render(request,'resultados_clientes.html', {'clientes':clientes})
    else:
        return render(request,'busqueda_clientes.html', {'mensaje':'Por favor, ingresá algún término de búsqueda'})

# Vista de eliminar

def eliminar_remate(request, id):
    remate=Remate.objects.get(id=id)
    remate.delete()
    remates=Remate.objects.all()
    remate_formulario=remateForm()
    mensaje='Remate eliminado'
    return render(request,'remates.html', {'mensaje':mensaje, 'formulario':remate_formulario, 'remates':remates})

# vista de editar

def editar_remate(request, id):
    if request.method=='POST':
        pass
    else:
        remate=Remate.objects.get(id=id)
        remate_formulario=remateForm(initial={'bien':remate.bien,'base':remate.base,'fecha':remate.fecha,'lugar':remate.lugar})
        return render(request,'editar_remate.html', {'formulario':remate_formulario, 'remates':remates})