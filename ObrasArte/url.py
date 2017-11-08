from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.listar_artista, name='listar_artista'),
    url(r'^pinturas/$', views.listar_pintura, name='listar_pintura'),
    url(r'^nueva/$', views.Artista_nuevo, name='Artista_nuevo'),
    url(r'^nueva/pintura$', views.Pintura_nueva, name='Pintura_nueva'),
    url(r'^artista/(?P<pk>\d+)/$', views.detalle_artista, name='detalle_artista'),
    url(r'^pinturas/(?P<pk>\d+)/$', views.detalle_pintura, name='detalle_pintura'),
    url(r'^editar/pintura(?P<pk>\d+)/$', views.editar_pintura, name='editar_pintura'),
    url(r'^eliminar/pintura(?P<pk>\d+)/$', views.eliminar_pintura, name='eliminar_pintura'),
    url(r'^eliminar/Artista(?P<pk>\d+)/$', views.eliminar_artista, name='eliminar_artista'),


    ]
