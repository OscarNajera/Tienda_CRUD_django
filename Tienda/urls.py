"""Tienda URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Articulos.views import index,tupedido,tucompra,login,registro,crearArticulo,GuardarArticulo,VerArticulos,VerArticulosHero,actualizar,Guardaractualizacion
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import LoginView,LogoutView




urlpatterns = [
    path('admin/', admin.site.urls),
    path('',index, name='inicio'),
    path('tupedido',tupedido, name='pedido'),
    path('tucompra',tucompra, name='compra'),
    
    #login de registro
    path('login',login, name='login'),
    path('registro',registro, name='registro'),
    
    ##almacenamiento de articulo
    path('crearArticulo',crearArticulo, name='crearArticulo'),
    path('GuardarArticulo/',GuardarArticulo, name='GuardarArticulo'),
    path('VerArticulos/',  VerArticulos, name="VerArticulos"),
    path('VerArticulosHero/',  VerArticulosHero, name="VerArticulosHero"),
    
    path("login/",LoginView.as_view(template_name='login.html'), name="login" ),
    path("logout/",LogoutView.as_view(template_name='logout.html'), name="logout" ),
    path('actualizar/<int:idx>',  actualizar, name="actualizar"),
    path('Guardaractualizacion/',  Guardaractualizacion, name="Guardaractualizacion"),
  
  ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
 










