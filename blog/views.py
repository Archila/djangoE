from django.shortcuts import render
from django.utils import timezone
from .models import Publicacion
# Create your views here.
def listar_publicacion(request):
    pub = Publicacion.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar_publicacion.html', {'pub': pub})
