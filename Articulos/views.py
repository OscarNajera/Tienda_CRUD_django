from django.shortcuts import render,HttpResponse,redirect     
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from .formulario import CrearUsuario 
from django.contrib import messages
from .models import Articulos,PedidoDE
from django.contrib.auth.forms import  UserCreationForm  


def index(request ):    
    articulos = Articulos.objects.all()
    return render(request,"index.html",{
              'articulos':articulos
      })

def tupedido(request ):    
    return render(request,"TuPedido.html" )

def tucompra(request ):    
    return render(request,"TuCompra.html" )

def login(request ):    
    return render(request,"login.html" )

def registrox(request ):    
    xformulario=CrearUsuario()
    if request.method == "POST":
        xformulario=CrearUsuario(request.POST)
        if xformulario.is_valid():
            xformulario.save()
            messages.success(request, "Usuario creado Exitosamente")
            return redirect("/")        
    else:
        xformulario=CrearUsuario()
        messages.success(request, "error al crear el usuario")
    return(request, 'registro.html',{"xformulario":xformulario}) 
            
 

def registro(request):
    xformulario=CrearUsuario()
    if request.method =="POST":
        xformulario=CrearUsuario(request.POST)
        if xformulario.is_valid():
            xformulario.save()
            
            messages.success(request, f"Usuario Crado" )
            return redirect("/")
    else:
        xformulario=CrearUsuario()
        messages.success(request, f"No se pudo crear el Xusuario" )
     
    return render(request, 'registro.html',{"xformulario":xformulario}) 


#Csoto2104

def crearArticulo(request):    
       return render(request, 'crearArticulo.html')
   

def GuardarArticulo(request):
    
    if request.method == 'POST':
        xnombre      =request.POST['nombre']
        xdescripcion =request.POST['descripcion']
        xprecio      =request.POST['precio']

        articulo = Articulos(
            nombre      = xnombre,
            descripcion = xdescripcion,
            precio      = xprecio,
 
        )  
        articulo.img= request.FILES.get('img')       
        
        
        articulo.save()
    else:
        return HttpResponse("No se puede crear el articulo")
    return HttpResponse("Articulo creado")

def VerArticulos(request):
    articulos = Articulos.objects.all()

    # articulos = Articulos.objects.all()
    return render(request,"mostrarArticulos.html",{
              'articulos':articulos
      })  
    
    

##Alonel #(Cindycuil --  Alonel123456)  
##123456  
def VerArticulosHero(request):
    articulos = Articulos.objects.all()
    # articulos = Articulos.objects.all()
    return render(request,"VerArticulosHero.html",{
              'articulos':articulos
      })  


def actualizar(request, idx):
    articulos = Articulos.objects.filter(pk=idx)
    return  render(request,"actualizar.html",{'articulos': articulos   }    )  
 
 
 
def Guardaractualizacion(request):
    
    
    if request.method == 'POST':
        pk  =request.POST['pk']
        articulos = Articulos.objects.get(pk=pk)
       
       
        xnombre      =request.POST['updatenombre']
        xdescripcion =request.POST['updatedescripcion']
        xprecio      =request.POST['updateprecio']
        
      
        articulos.nombre= xnombre
        articulos.precio= xdescripcion
        articulos.descripcion= xprecio
        articulos.img= request.FILES.get('updateimg') 
         
        articulos.save()      
 
    else:
        return HttpResponse("No se puede crear el articulo")
    return HttpResponse(f"Articulo Actualizado   <a href='/'>Inicio</a> <br>id    {articulos.nombre}")
  