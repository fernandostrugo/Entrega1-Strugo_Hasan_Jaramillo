from hashlib import new
from django.urls import path
from appblog.views import *
from django.contrib.auth.views import LogoutView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", inicio, name="inicio"),
    path("bienvenida/", bienvenida, name="entrar"),
    path("user/", user, name="usuario"),
    path("libros/", book, name="libro"),
    path("comentarios/", comment, name="comentario"),
    path("comentarioFormulario/", comentarioFormulario, name="comentarioFormulario"),
    path("libroFormulario/", libroFormulario, name="libroFormulario"),
    path("busquedaAutor/", busquedaAutor, name="busquedaAutor"),
    path("buscar/", buscar,),
    path("usuarioFormulario/", usuarioFormulario, name="usuarioFormulario"),
    path("busquedaComentario/", busquedaComentario, name="busquedaComentario"),
    path("buscarComentario/", buscarComentario,),
    path("busquedaUsuario/", busquedaUsuario, name="busquedaUsuario"),
    path("buscarUsuario/", buscarUsuario,),
    path('libro/list', LibroList.as_view(), name='List'),
    path(r'^(?P<pk>\d+)$', LibroDetalle.as_view(), name ='Detail'),
    path(r'^nuevo$', LibroCreacion.as_view(), name = 'New'),
    path(r'^edtiar/(?P<pk>\d+)$', LibroUpdate.as_view(), name = 'Edit'),
    path(r'^borrar/(?P<pk>\d+)$', LibroDelete.as_view(), name = 'Delete'),
    path('login/', login_request, name = 'Login'),
    path('logout/', LogoutView.as_view(template_name='appblog/logout.html'), name = 'Logout'),
    path('editarPerfil/', editar_perfil, name="EditarPerfil"),
    path('registrar/', registrar, name='registrar'),
    path('perfil/editar/', editar_perfil, name='editar_perfil'),
    path('perfil/', perfil, name='perfil'),
    path('abaut/', abaut, name='abaut'),
    path('perfil/cambiar-contrasenia/', CambiarContrasenia.as_view(), name='cambiar_contrasenia'),
 ]
    
urlpatterns+= static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
