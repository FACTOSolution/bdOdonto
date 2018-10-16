# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views
from django.views.generic import RedirectView

app_name = 'sistema_fichas'
urlpatterns = [
    url(r'^$', views.login, name='login'),
    url(r'^index/$', views.index, name='index'),
    url(r'^paciente/$', views.menu_paciente, name='menu_paciente'),
    url(r'^cadastrar_paciente/$', views.cadastrar_paciente, name='cadastrar_paciente'),
    url(r'^detalhar_paciente/$', views.detalhar_paciente, name='detalhar_paciente'),
    url(r'^listar_procedimento/$', views.listar_procedimentos, name='listar_procedimentos'),
    url(r'^cadastrar_procedimento/$', views.cadastrar_procedimento, name='cadastrar_procedimento'),
    url(r'^cadastrar_procedimento/opcoes_ficha/(?P<slug>[-\w]+)/$', views.opcoes_ficha, name='opcoes_ficha'),
    url(r'^listar_exames/$', views.listar_exames, name='listar_exames'),
    url(r'^listar_fichas/$', views.buscar_fichas_paciente, name='listar_fichas'),
    url(r'^detalhar_ficha/(?P<slug>[-\w]+)-(?P<pk>\d+)/$', views.detalhar_ficha, name='detalhar_ficha'),
    url(r'^detalhar_procedimento/(?P<pk>\d+)/$', views.detalhar_procedimento, name='detalhar_procedimento'),
    url(r'^listar_planejamentos/$', views.listar_planejamentos, name='listar_planejamentos'),
    url(r'^cadastrar_planejamento/$', views.cadastrar_planejamento, name='cadastrar_planejamento'),
    url(r'^logout/$', views.user_logout, name='logout'),
    url(r'^odontograma/$', views.odontograma, name='odontograma'),
    url(r'^listar_turmas/$', views.listar_turmas, name='listar_turmas'),
    url(r'^detalhar_turma/(?P<pk>[0-9]+)/$', views.detalhar_turma, name='detalhar_turma'),
    url(r'^info_ficha/(?P<pk>[0-9]+)/$', views.info_ficha, name='info_ficha'),
    url(r'^atendimento/$', views.atendimento, name='atendimento'),
    url(r'^atendimento_opcoes/$', views.atendimento_opcoes, name='atendimento_opcoes'),
    url(r'^diagnostico/$', views.diagnostico, name='diagnostico'),
    url(r'^ortodontia/$', views.ortodontia, name='ortodontia'),
    url(r'^periodontia/$', views.periodontia, name='periodontia'),
    url(r'^urgencia/$', views.urgencia, name='urgencia'),
    url(r'^endodontia/$', views.endodontia, name='endodontia'),
    url(r'^endodontia_tabela/$', views.endodontia_tabela, name='endodontia_tabela'),
    url(r'^ppr/$', views.ppr, name='ppr'),
    url(r'^dentistica/$', views.dentistica, name='dentistica'),
    url(r'^buscar_paciente/$', views.buscar_paciente, name='buscar_paciente'),

]
