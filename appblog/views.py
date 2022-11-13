from django.http import HttpResponse
from django.shortcuts import render, redirect
from appblog.models import *
from appblog.forms import *
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from appblog.models import EditarPerfilFormulario
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import PasswordChangeView
from appblog.models import ExtensionUsuario
from django.contrib.auth.views import PasswordChangeView




def inicio(request):
     return render(request, "appblog/index.html")

def bienvenida(request):
    return render(request, "appblog/bienvenida.html")

def abaut(request):
     return render(request, "appblog/abaut.html")

def user(request):
    users= Usuario.objects.all()
    return render(request, "appblog/usuarios.html",{'users':users})

def book(request):
    books= Libro.objects.all()
    return render(request, "appblog/libros.html",{'books':books})

def comment(request):
    comments= Comentario.objects.all()
    return render(request, "appblog/comentarios.html",{'comments':comments})

@login_required
def usuarioFormulario(request):
    if request.method == "POST":
        miFormulario2 = UsuarioFormulario(request.POST)
        print(miFormulario2)
        if miFormulario2.is_valid:
            informacion = miFormulario2.cleaned_data
            usuario =  Usuario (nombre=informacion["nombre"], apellido=informacion["apellido"], dni=informacion["dni"], nickname=informacion["nickname"], email=informacion["email"], fechaRegistro=datetime.now() )
            usuario.save()
            return render(request, "appblog/index.html")
    else:            
     miFormulario2 = UsuarioFormulario()       
    return render(request, "appblog/usuarioFormulario.html", {"miFormulario2":miFormulario2})

@login_required
def libroFormulario(request):
    if request.method == "POST":
        miFormulario = LibroFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            libro = Libro (titulo=informacion["titulo"], autor=informacion["autor"], genero=informacion["genero"], fechaIngreso=datetime.now())
            libro.save()
            return render(request, "appblog/index.html")
    else:        
     miFormulario = LibroFormulario()   
    return render(request, "appblog/libroFormulario.html", {"miFormulario":miFormulario})

@login_required
def comentarioFormulario(request):
    if request.method == "POST":
        miFormulario = ComentarioFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid:
            informacion = miFormulario.cleaned_data
            comentario = Comentario (creador=informacion["creador"], texto=informacion["texto"], fechaCreacion=datetime.now())
            comentario.save()
            return render(request, "appblog/index.html")
    else:        
     miFormulario = ComentarioFormulario()
    return render(request, "appblog/comentarioFormulario.html", {"miFormulario":miFormulario})

def busquedaAutor(request):
    return render(request, "appblog/busquedaAutor.html")
    
def busquedaUsuario(request):
    return render(request, "appblog/busquedaUsuario.html")   
    
def busquedaComentario(request):
    return render(request, "appblog/busquedaComentario.html")

def buscarUsuario(request):
    if request.GET["nickname"]:
    
        nickname = request.GET["nickname"]
        usuarios = Usuario.objects.filter(nickname__icontains=nickname)
        return render(request, "appblog/resultadosBusquedasUsuario.html", {"usuarios":usuarios, "nickname":nickname})
    else:   
        respuesta = "No enviaste Alias"
    return HttpResponse(respuesta)

def buscar(request):
    if request.GET["autor"]:
    
        autor = request.GET["autor"]
        libros = Libro.objects.filter(autor__icontains=autor)
        return render(request, "appblog/resultadosBusquedasAutor.html", {"libros":libros, "autor":autor})
    else:
        respuesta = "No enviaste datos"
    return HttpResponse(respuesta)
    
def buscarComentario(request):
    if request.GET["creador"]:
    
        creador = request.GET["creador"]
        comentarios = Comentario.objects.filter(creador__icontains=creador)
        return render(request, "appblog/resultadosBusquedasComentarios.html", {"comentarios":comentarios, "creador":creador})
    else:
        respuesta = "No enviaste creador"
    return HttpResponse(respuesta)

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.get_user()
            login(request, usuario)
            extensionUsuario, es_nuevo = ExtensionUsuario.objects.get_or_create(user=request.user)

            return redirect('inicio')
    else:
        form = AuthenticationForm()
    return render(request, "appblog/login.html", {'form':form})

def registrar(request):
    
    if request.method == 'POST':
        formulario = MiFormularioDeCreacion(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('inicio')
    else:
        formulario = MiFormularioDeCreacion()
    
    return render(request, 'appblog/registrar.html', {'formulario': formulario})

@login_required
def editar_perfil(request):
    
    user = request.user
    
    if request.method == 'POST':
        formulario = EditarPerfilFormulario(request.POST, request.FILES)

        if formulario.is_valid():
            data_nueva = formulario.cleaned_data
            user.first_name = data_nueva['first_name']
            user.last_name = data_nueva['last_name']
            user.email = data_nueva['email']
            user.extensionusuario.avatar = data_nueva['avatar']
            user.extensionusuario.save()
            user.save()
            return redirect('perfil')
        
    else:
        formulario = EditarPerfilFormulario(
            initial={
                'first_name': user.first_name,
                'last_name': user.last_name,
                'email': user.email,
                'avatar': user.extensionusuario.avatar,
            }
        )
    return render(request, 'appblog/editarPerfil.html', {'formulario': formulario})

@login_required
def perfil(request):
    return render(request, 'appblog/perfil.html', {})


class CambiarContrasenia(LoginRequiredMixin, PasswordChangeView):
    template_name = 'appblog/cambiar_contrasenia.html'
    success_url = '/appblog/perfil/'
    form_class = MiCambioDePassword