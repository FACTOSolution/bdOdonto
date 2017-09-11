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
    url(r'^info_ficha/(?P<pk>[0-9]+)/$', views.info_ficha, name='info_ficha'),
    url(r'^atendimento/$', views.atendimento, name='atendimento'),
    url(r'^atendimento_opcoes/$', views.atendimento_opcoes, name='atendimento_opcoes'),
    url(r'^redirecionar/$', views.redirecionar_atendimento, name='redirecionar_atendimento'),
    url(r'^diagnostico/$', views.diagnostico, name='diagnostico'),
    url(r'^ortodontia/$', views.ortodontia, name='ortodontia'),
    url(r'^periodontia/$', views.periodontia, name='periodontia'),
    url(r'^urgencia/$', views.urgencia, name='urgencia'),
    url(r'^endodontia/$', views.endodontia, name='endodontia'),
    url(r'^endodontia_tabela/$', views.endodontia_tabela, name='endodontia_tabela'),
    url(r'^ppr/$', views.ppr, name='ppr'),
    url(r'^dentistica/$', views.dentistica, name='dentistica'),
]
