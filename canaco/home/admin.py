from django.contrib import admin
from .models import Categoria, Archivo, Perfil, Publicacion, GaleriaPublicacion, Comentario


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'fk_user', 'createdat')
    search_fields = ('nombre',)


@admin.register(Archivo)
class ArchivoAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'tipo', 'tamano', 'fk_user', 'createdat')
    search_fields = ('nombre', 'nombre_temporal')


@admin.register(Perfil)
class PerfilAdmin(admin.ModelAdmin):
    list_display = ('user', 'apellido_paterno', 'apellido_materno')
    search_fields = ('user__username',)


class GaleriaPublicacionInline(admin.TabularInline):
    model = GaleriaPublicacion
    extra = 1


@admin.register(Publicacion)
class PublicacionAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'categoria', 'autor', 'estado', 'visitas', 'createdat', 'updatedat')
    list_filter = ('estado', 'categoria', 'createdat')
    search_fields = ('titulo', 'resumen', 'contenido')
    readonly_fields = ('visitas', 'createdat', 'updatedat')
    inlines = [GaleriaPublicacionInline]


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    list_display = ('publicacion', 'user', 'estado', 'createdat', 'updatedat')
    list_filter = ('estado', 'createdat')
    search_fields = ('contenido',)
