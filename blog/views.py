from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Publicacion
from .models import Post
# Create your views here.
#def listar_publicacion(request):
#    pub = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
#    return render(request, 'blog/listar_publicacion.html', {'pub': pub})

def listar_pub(request):
    pub = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/listar_publicacion.html', {'pub': pub})

def detalle_pub(request, pk):
    p=get_object_or_404(Post,pk= pk)
    return render(request,'blog/detalle_publicacion.html',{'p':p})
