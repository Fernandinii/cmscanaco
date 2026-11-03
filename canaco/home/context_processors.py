from home.models import Categoria, Publicacion, Perfil

def global_categorias(request):
    perfil_usuario = None
    if request.user.is_authenticated:
        perfil_usuario, _ = Perfil.objects.get_or_create(user=request.user)
    return {
        'global_categorias': Categoria.objects.all().order_by('nombre'),
        'global_recientes': Publicacion.objects.filter(
            estado=Publicacion.ESTADO_PUBLICADO
        ).select_related('imagen_portada').order_by('-createdat')[:3],
        'global_perfil_usuario': perfil_usuario,
    }
