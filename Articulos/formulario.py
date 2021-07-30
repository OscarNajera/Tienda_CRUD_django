from django import forms
from django.core import validators
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
 
class CrearUsuario(UserCreationForm):
    
    email = forms.EmailField(label="email")  
    password1 = forms.CharField(label= "contraseña",widget=forms.PasswordInput)
    password2 = forms.CharField(label= "Confirma contraseña",widget=forms.PasswordInput)
      
    class Meta:
        model=User
        fields=["username","email","password1","password2"]
        help_texts = {k:"" for k in fields}
    
    
 
    
    