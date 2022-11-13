from django.contrib import admin
from appblog.models import *
from appblog.models import ExtensionUsuario

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Libro)
admin.site.register(Comentario)
admin.site.register(ExtensionUsuario)