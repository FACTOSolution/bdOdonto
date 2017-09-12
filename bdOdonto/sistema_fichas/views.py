# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *
from .forms import *
import json

def index(request):
    return render(request, 'sistema_fichas/base.html', {})

@login_required
def lista_fichas_aluno(request):
    if request.method == 'POST':
        requested_aluno = get_object_or_404(Aluno, pk=request.POST['aluno_mat'])
        requested_turma = get_object_or_404(Turma, pk=request.POST['turma_code'])
        requested_rela = get_object_or_404(Turma_Aluno, turma=requested_turma, aluno=requested_aluno, periodo=request.POST['periodo'])
        requested_atendimentos = Atendimentos.objects.find(turma_aluno = requested_rela)
        ficha_lista = list()
    for atendi in requested_atendimentos:
        if atendi.tipo_ficha == 1:
            ficha_lista.append(get_object_or_404(Ficha_Diagnostico, codeA=atendi.code))
        else:
            pass
    return render(request, 'lista_fichas_aluno.html', {'fichas': ficha_lista})

@login_required
def user_logout(request):
    logout(request)
    if request.session.has_key('turma_atual'):
        del request.session['turma_atual']
    return HttpResponseRedirect('/accounts/login')
    
def registrar_usuario(request):
    if request.user.is_authenticated:
        return redirect('sistema_fichas:listar_turmas')
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        aluno_form = AlunoForm(data=request.POST)
        if user_form.is_valid() and aluno_form.is_valid():
            user = user_form.save(commit=False)
            aluno = aluno_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            aluno.usuario = user
            aluno.save()
            return redirect('/accounts/login')
    else:
        user_form = UserForm()
        aluno_form = AlunoForm()
	
    return render(request, 'sistema_fichas/registrar_usuario.html',
                  {'user_form': user_form,
                   'aluno_form': aluno_form})

def ficha_diagnostico(request):
    if request.method == "POST":
        form = Ficha_DiagnosticoForm(request.POST)
        if form.is_valid():
            ficha = form.save(commit=False)
            ficha.data = timezone.now()
            ficha.save()
            return redirect('sistema_fichas:ficha_diagnostico_detail', pk=ficha.pk)
        else:
            form = Ficha_DiagnosticoForm()
        return render(request, 'sistema_fichas/ficha_diagnostico_edit.html',
                      {'ficha': ficha})

@login_required
def listar_turmas(request):
    aluno = Aluno.objects.filter(usuario=request.user)
    turmas = Turma.objects.filter(alunos=aluno)
    return render(request, 'sistema_fichas/listar_turmas.html',
                  {'turmas' : turmas})

@login_required
def detalhar_turma(request, pk):

    if request.session.has_key('turma_atual'):
        del request.session['turma_atual']
        request.session.modified = True
    
    turma = get_object_or_404(Turma, pk=pk)
    fichas = Tipo_Ficha.objects.filter(turma=turma)
    request.session['turma_atual'] = turma.codigo
    request.session.modified = True
    return render(request, 'sistema_fichas/detalhar_turma.html',
                  {'fichas' : fichas},
                  {'turma': turma})

@login_required
def info_ficha(request, pk):
    ficha = get_object_or_404(Tipo_Ficha, pk=pk)
    request.session['ficha_atual'] = ficha.nome
    request.session.modified = True
    codigo_turma = request.session['turma_atual']
    turma = get_object_or_404(Turma, codigo=codigo_turma)
    aluno = get_object_or_404(Aluno, usuario=request.user)
    usuario = aluno.usuario
    return render(request, 'sistema_fichas/info_ficha.html',
                  {'ficha' : ficha,
                   'turma': turma,
                   'aluno': usuario})

@login_required
def atendimento(request):
    if request.method == 'POST':
        atendimento_form = AtendimentoForm(data=request.POST)
        paciente_form = PacienteForm(data=request.POST)
        if paciente_form.is_valid() and atendimento_form.is_valid():
            aluno = get_object_or_404(Aluno, usuario=request.user)
            t_codigo = request.session['turma_atual']
            turma = get_object_or_404(Turma, codigo=t_codigo)
            turma_aluno = get_object_or_404(Turma_Aluno, turma=turma, aluno=aluno)
            ficha_pk = request.session['ficha_atual']
            ficha = get_object_or_404(Tipo_Ficha, nome=ficha_pk)
            paciente = paciente_form.save()
            paciente.save()
            atendimento = atendimento_form.save(commit=False)
            atendimento.turma_aluno = turma_aluno
            atendimento.tipo_ficha = ficha
            atendimento.paciente = paciente
            atendimento.save()
            request.session['paciente_atual'] = paciente.cpf
            return redirect('sistema_fichas:atendimento_opcoes')
    else:
        atendimento_form = AtendimentoForm()
        paciente_form = PacienteForm()
    return render(request, 'sistema_fichas/atendimento.html',
                  {'atendimento_form': atendimento_form,
                   'paciente_form': paciente_form})

##def verify_ficha(nome_ficha):
##    if nome_ficha == "Ficha Diagnostico":
##        aux = Ficha_DiagnosticoForm()
##        return aux
##    elif nome_ficha == "Ficha Ortodontia":
##        aux = Ficha_OrtondontiaForm()
##        return aux
##    elif nome_ficha == "Ficha Periodontia":
##        aux = Ficha_PeriodontiaForm()
##        return aux
##    elif nome_ficha == "Ficha Urgencia":
##        aux = Ficha_UrgenciaForm()
##        return aux
##    elif nome_ficha == "Ficha Endodontia":
##        aux = Ficha_EndodontiaForm()
##        return aux
##    elif nome_ficha == "Ficha Endodontia Tabela":
##        aux = Ficha_Endodontia_Tabela()
##        return Ficha_Endodontia_Tabela
##    elif nome_ficha == "Ficha PPR":
##        aux = Ficha_PPRForm()
##        return aux
##    elif nome_ficha == "Ficha Dentistica":
##        aux = Ficha_DentisticaForm()
##        return aux
##    else:
##        return None

@login_required
def atendimento_opcoes(request):
    atendimento_ficha = False
    odontograma = False
    if request.session.has_key('atendimento_ficha'):
        atendimento_ficha = True
    if request.session.has_key('odontograma'):
        odontograma = True
    aluno = get_object_or_404(Aluno, usuario=request.user)
    t_codigo = request.session['turma_atual']
    turma = get_object_or_404(Turma, codigo=t_codigo)
    turma_aluno = get_object_or_404(Turma_Aluno, turma=turma, aluno=aluno)
    ficha_pk = request.session['ficha_atual']
    tipo_ficha = get_object_or_404(Tipo_Ficha, nome=ficha_pk)
    paciente = get_object_or_404(Paciente, cpf=request.session['paciente_atual'])
    atendimento = get_object_or_404(Atendimento, turma_aluno=turma_aluno, tipo_ficha=tipo_ficha, paciente=paciente)
    return render(request, 'sistema_fichas/atendimento_opcoes.html',
                  {'turma': turma,
                   'aluno': aluno,
                   'ficha': tipo_ficha,
                   'atendimento': atendimento,
                   'ficha_preenchida': atendimento_ficha,
                   'odontograma': odontograma})

@login_required
def odontograma(request):
    if request.method == 'POST' and request.is_ajax():
        aluno = get_object_or_404(Aluno, usuario=request.user)
        t_codigo = request.session['turma_atual']
        turma = get_object_or_404(Turma, codigo=t_codigo)
        turma_aluno = get_object_or_404(Turma_Aluno, turma=turma, aluno=aluno)
        ficha_pk = request.session['ficha_atual']
        tipo_ficha = get_object_or_404(Tipo_Ficha, nome=ficha_pk)
        paciente = get_object_or_404(Paciente, cpf=request.session['paciente_atual'])
        atendimento = get_object_or_404(Atendimento, turma_aluno=turma_aluno, tipo_ficha=tipo_ficha, paciente=paciente)
        odontograma_form = OdontogramaForm()
        pontos_json = json.loads(request.body.decode("utf-8"))
        odontograma = odontograma_form.save(commit=False)
        odontograma.pontos = pontos_json
        odontograma.atendimento = atendimento
        odontograma.save()
        request.session['odontograma'] = atendimento.paciente.nome
    return render(request, 'sistema_fichas/odontograma.html')

##@login_required
##def odontograma(request):
##    ficha_nome = request.session['ficha_atual']
##    ficha = verify_url(ficha.nome)
##    if request.method == 'POST':
##        aluno = get_object_or_404(Aluno, usuario=request.user)
##        t_codigo = request.session['turma_atual']
##        turma = get_object_or_404(Turma, codigo=t_codigo)
##        turma_aluno = get_object_or_404(Turma_Aluno, turma=turma, aluno=aluno)
##        ficha_pk = request.session['ficha_atual']
##        tipo_ficha = get_object_or_404(Tipo_Ficha, nome=ficha_pk)
##        atendimento = get_object_or_404(Atendimento, turma_aluno=turma_aluno, tipo_ficha=ficha)
##        
##    return render(request, 'sistema_fichas/odontograma.html')

@login_required
def redirecionar_atendimento(request):
    nome_ficha = request.session['ficha_atual']
    
    if nome_ficha == "Ficha Diagnostico":
        return redirect('sistema_fichas:diagnostico')
    elif nome_ficha == "Ficha Ortodontia":
        return redirect('sistema_fichas:ortodontia')
    elif nome_ficha == "Ficha Periodontia":
        return redirect('sistema_fichas:periodontia')
    elif nome_ficha == "Ficha Urgencia":
        return redirect('sistema_fichas:urgencia')
    elif nome_ficha == "Ficha Endodontia":
        return redirect('sistema_fichas:endodontia')
    elif nome_ficha == "Ficha Endodontia Tabela":
        return redirect('sistema_fichas:endodontia_tabela')
    elif nome_ficha == "Ficha PPR":
        return redirect('sistema_fichas:ppr')
    elif nome_ficha == "Ficha Dentistica":
        return redirect('sistema_fichas:dentistica')
    else:
        return redirect('sistema_fichas:atendimento_opcoes')

@login_required
def diagnostico(request):
    if request.method == 'POST':
        aluno = get_object_or_404(Aluno, usuario=request.user)
        t_codigo = request.session['turma_atual']
        turma = get_object_or_404(Turma, codigo=t_codigo)
        turma_aluno = get_object_or_404(Turma_Aluno, turma=turma, aluno=aluno)
        ficha_pk = request.session['ficha_atual']
        tipo_ficha = get_object_or_404(Tipo_Ficha, nome=ficha_pk)
        atendimento = get_object_or_404(Atendimento, turma_aluno=turma_aluno, tipo_ficha=tipo_ficha)
        ficha_form = Ficha_DiagnosticoForm(data=request.POST)
        if ficha_form.is_valid():
            ficha = ficha_form.save(commit=False)
            ficha.atendimento = atendimento
            ficha.save()
            request.session['atendimento_ficha'] = ficha_pk
            return redirect('sistema_fichas:atendimento_opcoes')
    else:
        ficha_form = Ficha_DiagnosticoForm()
    return render(request, 'sistema_fichas/diagnostico.html',
                  {'ficha_form': ficha_form})

@login_required
def urgencia(request):
    if request.method == 'POST':
        aluno = get_object_or_404(Aluno, usuario=request.user)
        t_codigo = request.session['turma_atual']
        turma = get_object_or_404(Turma, codigo=t_codigo)
        turma_aluno = get_object_or_404(Turma_Aluno, turma=turma, aluno=aluno)
        ficha_pk = request.session['ficha_atual']
        tipo_ficha = get_object_or_404(Tipo_Ficha, nome=ficha_pk)
        atendimento = get_object_or_404(Atendimento, turma_aluno=turma_aluno, tipo_ficha=tipo_ficha)
        ficha_form = Ficha_UrgenciaForm(data=request.POST)
        if ficha_form.is_valid():
            ficha = ficha_form.save(commit=False)
            ficha.atendimento = atendimento
            ficha.save()
            request.session['atendimento_ficha'] = ficha_pk
            return redirect('sistema_fichas:atendimento_opcoes')
    else:
        ficha_form = Ficha_UrgenciaForm()
    return render(request, 'sistema_fichas/urgencia.html',
                  {'ficha_form': ficha_form})

@login_required
def ortodontia(request):
    if request.method == 'POST':
        aluno = get_object_or_404(Aluno, usuario=request.user)
        t_codigo = request.session['turma_atual']
        turma = get_object_or_404(Turma, codigo=t_codigo)
        turma_aluno = get_object_or_404(Turma_Aluno, turma=turma, aluno=aluno)
        ficha_pk = request.session['ficha_atual']
        tipo_ficha = get_object_or_404(Tipo_Ficha, nome=ficha_pk)
        atendimento = get_object_or_404(Atendimento, turma_aluno=turma_aluno, tipo_ficha=tipo_ficha)
        ficha_form = Ficha_OrtodontiaForm(data=request.POST)
        if ficha_form.is_valid():
            ficha = ficha_form.save(commit=False)
            ficha.atendimento = atendimento
            ficha.save()
            request.session['atendimento_ficha'] = ficha_pk
            return redirect('sistema_fichas:atendimento_opcoes')
    else:
        ficha_form = Ficha_OrtodontiaForm()
    return render(request, 'sistema_fichas/ortodontia.html', 
                  {'ficha_form': ficha_form})

@login_required
def periodontia(request):
    if request.method == 'POST':
        aluno = get_object_or_404(Aluno, usuario=request.user)
        t_codigo = request.session['turma_atual']
        turma = get_object_or_404(Turma, codigo=t_codigo)
        turma_aluno = get_object_or_404(Turma_Aluno, turma=turma, aluno=aluno)
        ficha_pk = request.session['ficha_atual']
        tipo_ficha = get_object_or_404(Tipo_Ficha, nome=ficha_pk)
        atendimento = get_object_or_404(Atendimento, turma_aluno=turma_aluno, tipo_ficha=tipo_ficha)
        ficha_form = Ficha_PeriodontiaForm(request.POST)
        if ficha_form.is_valid():
            ficha = ficha_form.save(commit=False)
            ficha.atendimento = atendimento
            ficha.save()
            request.session['atendimento_ficha'] = ficha_pk
            return redirect('sistema_fichas:atendimento_opcoes')
    else:
        ficha_form = Ficha_PeriodontiaForm()
    return render(request, 'sistema_fichas/periodontia.html',
                  {'ficha_form': ficha_form})

@login_required
def endodontia(request):
    if request.method == 'POST':
        aluno = get_object_or_404(Aluno, usuario=request.user)
        t_codigo = request.session['turma_atual']
        turma = get_object_or_404(Turma, codigo=t_codigo)
        turma_aluno = get_object_or_404(Turma_Aluno, turma=turma, aluno=aluno)
        ficha_pk = request.session['ficha_atual']
        tipo_ficha = get_object_or_404(Tipo_Ficha, nome=ficha_pk)
        atendimento = get_object_or_404(Atendimento, turma_aluno=turma_aluno, tipo_ficha=tipo_ficha)
        ficha_form = Ficha_EndodontiaForm(request.POST)
        if ficha_form.is_valid():
            ficha = ficha_form.save(commit=False)
            ficha.atendimento = atendimento
            ficha.save()
            request.session['atendimento_ficha'] = ficha_pk
            return redirect('sistema_fichas:atendimento_opcoes')
    else:
        ficha_form = Ficha_EndodontiaForm()
    return render(request, 'sistema_fichas/endodontia.html',
                  {'ficha_form': ficha_form})

@login_required
def endodontia_tabela(request):
    if request.method == 'POST':
        aluno = get_object_or_404(Aluno, usuario=request.user)
        t_codigo = request.session['turma_atual']
        turma = get_object_or_404(Turma, codigo=t_codigo)
        turma_aluno = get_object_or_404(Turma_Aluno, turma=turma, aluno=aluno)
        ficha_pk = request.session['ficha_atual']
        tipo_ficha = get_object_or_404(Tipo_Ficha, nome=ficha_pk)
        atendimento = get_object_or_404(Atendimento, turma_aluno=turma_aluno, tipo_ficha=tipo_ficha)
        ficha_form = Ficha_Endodontia_TabelaForm(request.POST)
        if ficha_form.is_valid():
            ficha = ficha_form.save(commit=False)
            ficha.atendimento = atendimento
            ficha.save()
            request.session['atendimento_ficha'] = ficha_pk
            return redirect('sistema_fichas:atendimento_opcoes')
    else:
        ficha_form = Ficha_Endodontia_TabelaForm()
    return render(request, 'sistema_fichas/endodontia_tabela.html',
                  {'ficha_form': ficha_form})

@login_required
def ppr(request):
    if request.method == 'POST':
        aluno = get_object_or_404(Aluno, usuario=request.user)
        t_codigo = request.session['turma_atual']
        turma = get_object_or_404(Turma, codigo=t_codigo)
        turma_aluno = get_object_or_404(Turma_Aluno, turma=turma, aluno=aluno)
        ficha_pk = request.session['ficha_atual']
        tipo_ficha = get_object_or_404(Tipo_Ficha, nome=ficha_pk)
        atendimento = get_object_or_404(Atendimento, turma_aluno=turma_aluno, tipo_ficha=tipo_ficha)
        ficha_form = Ficha_PPRForm(request.POST)
        if ficha_form.is_valid():
            ficha = ficha_form.save(commit=False)
            ficha.atendimento = atendimento
            ficha.save()
            request.session['atendimento_ficha'] = ficha_pk
            return redirect('sistema_fichas:atendimento_opcoes')
    else:
        ficha_form = Ficha_PPRForm()
    return render(request, 'sistema_fichas/ppr.html',
                  {'ficha_form': ficha_form})

@login_required
def dentistica(request):
    if request.method == 'POST':
        aluno = get_object_or_404(Aluno, usuario=request.user)
        t_codigo = request.session['turma_atual']
        turma = get_object_or_404(Turma, codigo=t_codigo)
        turma_aluno = get_object_or_404(Turma_Aluno, turma=turma, aluno=aluno)
        ficha_pk = request.session['ficha_atual']
        tipo_ficha = get_object_or_404(Tipo_Ficha, nome=ficha_pk)
        atendimento = get_object_or_404(Atendimento, turma_aluno=turma_aluno, tipo_ficha=tipo_ficha)
        ficha_form = Ficha_DentisticaForm(request.POST)
        if ficha_form.is_valid():
            ficha = ficha_form.save(commit=False)
            ficha.atendimento = atendimento
            ficha.save()
            request.session['atendimento_ficha'] = ficha_pk
            return redirect('sistema_fichas:atendimento_opcoes')
    else:
        ficha_form = Ficha_DentisticaForm()
    return render(request, 'sistema_fichas/dentistica.html',
                  {'ficha_form': ficha_form})
