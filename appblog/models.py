from django.db import models
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from django.views.generic.edit import DeleteView
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import PasswordChangeForm



class Usuario(models.Model):
    nombre=models.CharField(max_length=30)
    apellido=models.CharField(max_length=30)
    dni=models.IntegerField(primary_key=True)
    nickname=models.CharField(max_length=30)
    email=models.EmailField()
    fechaRegistro=models.DateTimeField()

    def __str__(self):
        return f"{(self.nombre)}-{(self.apellido)} | {(self.dni)}" 


class Libro(models.Model):
    titulo=models.CharField(max_length=80)
    autor=models.CharField(max_length=30)
    genero=models.CharField(max_length=30)
    fechaIngreso=models.DateTimeField()

    def __str__(self):
        return f"Titulo:{(self.titulo)} | Autor:{(self.autor)} | Genero:{(self.genero)} | fechaIngreso:{(self.fechaIngreso.strftime('%d %b, %Y'))}"   ##.strftime('%d %b, %Y')

class Comentario(models.Model):
    id=models.IntegerField(primary_key=True)
    creador=models.CharField(max_length=30)
    texto=models.CharField(max_length=5000)
    fechaCreacion=models.DateTimeField()

    def __str__(self):
        return f"{(self.id)}-{(self.creador)} | {(self.fechaCreacion.strftime('%d %b, %Y'))}"

class LibroList(ListView):
    model = Libro
    template_name = "appblog/libros_list.html"
    
class LibroDetalle(DetailView):
    model = Libro
    template_name = "appblog/libro_detalle.html"

class LibroCreacion(CreateView):
    model = Libro
    success_url = "/appblog/libro/list"
    fields = ['titulo', 'autor', 'genero', 'fechaIngreso']

class LibroUpdate(UpdateView):
    model = Libro
    success_url = "/appblog/libro/list"
    fields = ['titulo', 'autor', 'genero', 'fechaIngreso']
    
class LibroDelete(DeleteView):
    model = Libro
    success_url = "/appblog/libro/list"
    
class EditarPerfilFormulario(forms.Form):
    email = forms.CharField()
    first_name = forms.CharField(label='Nombre')
    last_name = forms.CharField(label='Apellido')
    avatar = forms.ImageField(required=False)
    
class MiFormularioDeCreacion(UserCreationForm):
    
    email = forms.CharField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput) 
    password2 = forms.CharField(label='Repetir Contraseña', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
        help_texts = {key: '' for key in fields}

class ExtensionUsuario(models.Model):
    avatar = models.ImageField(upload_to='avatares',null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    
class MiCambioDePassword(PasswordChangeForm):
    old_password = forms.CharField(label='Contrasenia vieja', widget=forms.PasswordInput) 
    new_password1 = forms.CharField(label='Contrasenia nueva', widget=forms.PasswordInput)
    new_password2 = forms.CharField(label='Repetir Contrasenia nueva', widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['old_password', 'new_password1', 'new_password2']
        help_texts = {key: '' for key in fields}