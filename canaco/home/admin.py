from django.contrib import admin
from .models import Categoria, Noticia, Comentario, Perfil


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'registrado_por', 'fecha_registro')
    search_fields = ('nombre',)
    list_filter = ('fecha_registro',)


@admin.register(Noticia)
class NoticiaAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'categoria', 'estado', 'visitas', 'fecha_creacion', 'fecha_actualizacion')
    list_filter = ('estado', 'categoria', 'fecha_creacion')
    search_fields = ('titulo', 'contenido')
    readonly_fields = ('visitas', 'fecha_creacion', 'fecha_actualizacion')


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('noticia', 'usuario', 'aprobado', 'fecha')
    list_filter = ('aprobado', 'fecha')
    search_fields = ('contenido',)


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'telefono', 'fecha_registro')
    search_fields = ('usuario__username',)
