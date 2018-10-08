# -*- coding: utf-8 -*-
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.urls import reverse
from .models import *
from .forms import *
import json

def login(request):
    if request.method == 'POST':    
        #form = AuthenticationForm(data=request.POST) # Veja a documentacao desta funcao
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return HttpResponseRedirect('index') # redireciona o usuario logado para a pagina inicial
        else:
            return render(request, "registration/login.html", {'err': True})
    
    #se nenhuma informacao for passada, exibe a pagina de login com o formulario
    return render(request, "registration/login.html", {})


@login_required
def index(request):
    if request.method == 'GET':
        username = request.user.username
        return render(request, 'sistema_fichas/index.html', {'username': username})
    elif request.method == 'POST':
        cpf_p = request.POST['cpf_p']
        try:
            Paciente.objects.get(pk=cpf_p)
            request.session['cpf_p'] = cpf_p

            return HttpResponseRedirect(reverse('sistema_fichas:menu_paciente'))
        except Paciente.DoesNotExist:
            return render(request, 'sistema_fichas/paciente_nao_encontrado.html',  {'cpf': cpf_p})
            

@login_required
def menu_paciente(request):
    cpf_p = request.session.get('cpf_p', None)
    paciente = Paciente.objects.get(pk=cpf_p)
    qt_procedimentos = len(Procedimento.objects.filter(cpf_p=paciente.cpf))
    contexto = {'nome_p': paciente.nome,
                'cpf_p': paciente.cpf,
                'qt_procedimentos': qt_procedimentos,}
    return render(request, 'sistema_fichas/menu_paciente.html', context=contexto)

@login_required
def cadastrar_paciente(request):
    if request.method == 'GET':
        formPaciente = PacienteForm()
    elif request.method == 'POST':
        formPaciente = PacienteForm(request.POST, request.FILES)
        if formPaciente.is_valid():
            novo_paciente = formPaciente.save()
            request.session['cpf_p'] = novo_paciente.cpf
            return HttpResponseRedirect(reverse('sistema_fichas:menu_paciente'))            
    
    return render(request, 'sistema_fichas/cadastrar_paciente.html', {'form': formPaciente})

def detalhar_paciente(request):
    cpf_p = request.session['cpf_p']
    paciente = Paciente.objects.get(pk=cpf_p)
    formPaciente = PacienteForm(instance=paciente)
    return render(request, 'sistema_fichas/detalhes_paciente.html', {'form': formPaciente})

@login_required
def lista_fichas_aluno(request):
    if request.method == 'POST':
        requested_aluno = get_object_or_404(Aluno, pk=request.POST['aluno_mat'])
        requested_turma = get_object_or_404(Turma, pk=request.POST['turma_code'])
        requested_rela = get_object_or_404(Turma_Aluno, turma=requested_turma, aluno=requested_aluno, periodo=request.POST['periodo'])
        requested_atendimentos = Atendimento.objects.find(turma_aluno = requested_rela)
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
    return HttpResponseRedirect(reverse('sistema_fichas:login'))

'''def registrar_usuario(request):
    if request.user.is_authenticated:
        return redirect('sistema_fichas:listar_turmas')
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        aluno_form = AlunoForm(data=request.POST)
        if user_form.is_valid() and aluno_form.is_valid():
            user = user_form.save(commit=False)
            aluno = aluno_form.save(commit=False)
            password = user.password
            password
            user.set_password(user.password)
            user.save()
            aluno.usuario = user
            aluno.save()
            context = {'Flag': True}
            return render(request, "registration/login.html", context)
    else:
        user_form = UserForm()
        aluno_form = AlunoForm()
    return render(request, 'sistema_fichas/registrar_usuario.html',
                  {'user_form': user_form,
                   'aluno_form': aluno_form})'''

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
    aluno = get_object_or_404(Aluno, usuario=request.user) #???
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

@login_required
def atendimento_opcoes(request):
    aluno = get_object_or_404(Aluno, usuario=request.user)
    
    t_codigo = request.session['turma_atual']
    turma = get_object_or_404(Turma, codigo=t_codigo)

    turma_aluno = get_object_or_404(Turma_Aluno, turma=turma, aluno=aluno)

    ficha_pk = request.session['ficha_atual']
    tipo_ficha = get_object_or_404(Tipo_Ficha, nome=ficha_pk)

    cpf = request.session['paciente_atual']
    paciente = get_object_or_404(Paciente, cpf=cpf)

    atendimento = get_object_or_404(Atendimento, turma_aluno=turma_aluno, tipo_ficha=tipo_ficha, paciente=paciente)

    atendimento_ficha = False
    odontograma = False
    if request.session.has_key('atendimento_ficha'):
        atendimento_ficha = True
    if Odontograma.objects.filter(atendimento=atendimento):
        odontograma = True
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
        return redirect('sistema_fichas:atendimento_opcoes')
    return render(request, 'sistema_fichas/odontograma.html')

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


@login_required
def buscar_paciente(request):
    form = BuscarPaciente()
    if request.method == "POST":
        form = BuscarPaciente(request.POST)
        if form.is_valid():
            cpf = form.cleaned_data['cpf']
            try:
                paciente = Paciente.objects.get(pk=cpf)
                request.session['paciente_atual'] = paciente.cpf
                return redirect('sistema_fichas:atendimento_opcoes')
            except Exception as e:
                return redirect('sistema_fichas:atendimento')
    else:
        form = BuscarPaciente()
    return render(request, 'sistema_fichas/buscar_paciente.html', 
                  {'form': form})


def listar_fichas(atendimento):
    listas = []
    listas.append(get_object_or_404(Ficha_Diagnostico, atendimento=atendimento))
    listas.append(get_object_or_404(Ficha_Ortodontia, atendimento=atendimento))
    listas.append(get_object_or_404(Ficha_Periodontia, atendimento=atendimento))
    listas.append(get_object_or_404(Ficha_Urgencia, atendimento=atendimento))
    listas.append(get_object_or_404(Ficha_Endodontia, atendimento=atendimento))
    listas.append(get_object_or_404(Ficha_Endodontia_Tabela, atendimento=atendimento))
    listas.append(get_object_or_404(Ficha_PPR, atendimento=atendimento))
    listas.append(get_object_or_404(Ficha_Dentistica, atendimento=atendimento))
    return listas

#Listar as fichas do paciente com base no CPF 
#Fluxo: buscar_paciente
#Action: listar_fichas_paciente 
@login_required
def buscar_fichas_paciente(request):
    aluno = get_object_or_404(Aluno, usuario=request.user)
    t_codigo = request.session['turma_atual']
    turma = get_object_or_404(Turma, codigo=t_codigo)
    turma_aluno = get_object_or_404(Turma_Aluno, turma=turma, aluno=aluno)
    ficha_pk = request.session['ficha_atual']
    tipo_ficha = get_object_or_404(Tipo_Ficha, nome=ficha_pk)
    cpf = request.session['paciente_atual']
    paciente = get_object_or_404(Paciente, cpf=cpf)
    atendimento = get_object_or_404(Atendimento, turma_aluno=turma_aluno, tipo_ficha=tipo_ficha, paciente=paciente)
    listas = listar_fichas(atendimento)
    return render(request, 'sistema_fichas/listar_fichas_paciente.html', 
                  {'listas': listas})

#Histórico da ficha específica na turma selecionada
#Fluxo: detalhar_turma
#Action: historico_fichapass
@login_required
def historico_fichas_turma(request):
    pass

