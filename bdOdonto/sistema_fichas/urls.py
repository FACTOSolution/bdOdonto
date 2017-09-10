from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

app_name = 'sistema_fichas'
urlpatterns = [
    url(r'^odontograma/$', views.odontograma, name='odontograma'),
    url(r'^index/$', views.index, name='index'),
    url(r'^registro/$', views.registrar_usuario, name='registrar_usuario'),
    url(r'^turmas_aluno/$', views.listar_turmas, name='listar_turmas'),
    url(r'^detalhar_turma/(?P<pk>[0-9]+)/$', views.detalhar_turma, name='detalhar_turma'),
    url(r'^ficha/(?P<pk>[0-9]+)/$', views.ficha, name='ficha'),
]
