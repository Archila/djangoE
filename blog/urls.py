from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^$', views.listar_pub, name='index'),
        url(r'^postea/(?P<pk>[0-9]+)/$', views.detalle_pub,name='postea'),
        url(r'^post/new/$', views.post_new, name='post_new'),
        url(r'^post/edit/(?P<pk>[0-9]+)/$', views.post_edit, name='post_edit'),
]
