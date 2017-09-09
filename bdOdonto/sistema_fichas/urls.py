from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

app_name = 'sistema_fichas'
urlpatterns = [
    url(r'^odontograma/$', views.odontograma, name='odontograma'),
	url(r'^index/$', views.index, name='index'),
	url(r'^registro/$', views.registrar_usuario, name='registrar_usuario')
]
