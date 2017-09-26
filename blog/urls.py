from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.listar_pub, name='index'),
        url(r'^postea/(?P<pk>[0-9]+)/$', views.detalle_pub,name='postea'),
        url(r'^post/new/$', views.post_new, name='post_new'),
        url(r'^post/edit/(?P<pk>[0-9]+)/$', views.post_edit, name='post_edit'),
        url(r'^borrador/$', views.lista_borradores, name='lista_borradores'),
        url(r'^post/(?P<pk>\d+)/publish/$', views.postear_publicacion, name='postear_publicacion'),
        url(r'^post/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),
]
