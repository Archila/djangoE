from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Publicacion
from .models import Post
from .forms import PostForm
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

def post_new (request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('postea', pk=post.pk)
    else:
        form = PostForm()
        return render(request,'blog/post_edit.html',{'form':form})

def post_edit (request, pk):
    post = get_object_or_404(Post,pk= pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('postea', pk=post.pk)
    else:
        form = PostForm(instance=post)
        return render(request,'blog/post_edit.html',{'form':form})

def lista_borradores(request):
    posts = Post.objects.filter(published_date__isnull=True).order_by('created_date')
    return render(request, 'blog/borradores.html', {'posts': posts})

def postear_publicacion(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.publish()
    return redirect('postea ', pk=pk)

def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
    return redirect('index')
