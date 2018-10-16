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

def listar_procedimentos(request):
    list_proc = Procedimento.objects.filter(cpf_p = request.session['cpf_p'])
    return render(request, 'sistema_fichas/listar_procedimentos.html', {'procedimentos':list_proc})

def cadastrar_procedimento(request):
    if request.method == 'GET':
        formProcedimento = ProcedimentoForm()
    elif request.method == 'POST':
        aluno_user = request.user.username
        user = User.objects.filter(username = aluno_user)[0]
        
        aluno = Aluno.objects.get(usuario_id=user.id)
        
        turma = request.POST['materia']
        tap = TAP.objects.get(turma = turma, mat_aluno=aluno.matricula)
        cpf_p = request.session['cpf_p']
        paciente = Paciente.objects.get(pk=cpf_p)
        
        parc_procedimento = Procedimento(tap = tap, cpf_p = paciente)
        formProcedimento = ProcedimentoForm(request.POST, request.FILES, instance=parc_procedimento)


        if formProcedimento.is_valid():
            if formProcedimento.cleaned_data['exame']:
                if len(request.FILES) != 0:
                    imagem = request.FILES['exame_img']
                    parc_exame = Exame(cpf_p = paciente, imagem=imagem)
                    parc_exame.save()
                else:
                    return render(request, 'sistema_fichas/cadastrar_procedimento.html', {'form': formProcedimento, 'err_upload': True})
            procedimento = formProcedimento.save()
            if formProcedimento.cleaned_data['ficha_ou_procedimento']:
                materia = turma.replace(" ", "")
                request.session['procedimento'] = procedimento.id
                return HttpResponseRedirect(reverse('sistema_fichas:opcoes_ficha', args=(materia,)))
            return HttpResponseRedirect(reverse('sistema_fichas:listar_procedimentos'))
    return render(request, 'sistema_fichas/cadastrar_procedimento.html', {'form': formProcedimento, 'err_upload': False})

def opcoes_ficha(request, slug):
    materias = {
        'EstágioI':('Periodontia', 'Dentistica', 'PPR', 'Odontograma'),
        'EstágioII':('Periodontia', 'Dentistica', 'Endodontia', 'PPR', 'Odontograma'),
        'EstágioIII':('Periodontia', 'Dentistica', 'Endodontia', 'PPR', 'Odontograma', 'Urgencia'),
        'EstágioIV':('Periodontia', 'Dentistica', 'Endodontia', 'PPR', 'Odontograma', 'Urgencia', 'Ortodontia'),
        'PerioII':('Periodontia'),
        'DestísticaII':('Destística'),
        'DestísticaIV':('Destística'),
        'EndoII':('Endodontia'),
        'PPRI':('PPR'),
        'PT':('Odontograma'),
        'PFII':('Odontograma'),
        'Diagnóstico':('Diagnóstico'),
        'CirurgiaI':('Odontograma'),
        'CirurgiaII':('Odontograma'),
        'OrtoII':('Ortodontia'),
        }
    if request.method == 'GET':
        return render(request, 'sistema_fichas/opcoes_ficha.html', {'fichas': materias[slug], 'materia': slug})
    elif request.method == 'POST':
        nome_ficha = request.POST['TipoFicha']
        if nome_ficha == "Diagnóstico":
            return redirect('sistema_fichas:diagnostico')
        elif nome_ficha == "Ortodontia":
            return redirect('sistema_fichas:ortodontia')
        elif nome_ficha == "Periodontia":
            return redirect('sistema_fichas:periodontia')
        elif nome_ficha == "Urgencia":
            return redirect('sistema_fichas:urgencia')
        elif nome_ficha == "Endodontia":
            return redirect('sistema_fichas:endodontia')
        elif nome_ficha == "Endodontia Tabela":
            return redirect('sistema_fichas:endodontia_tabela')
        elif nome_ficha == "PPR":
            return redirect('sistema_fichas:ppr')
        elif nome_ficha == "Dentistica":
            return redirect('sistema_fichas:dentistica')
        elif nome_ficha == "Odontograma":
            return redirect('sistema_fichas:odontograma')
        else:
            return redirect('sistema_fichas:atendimento_opcoes')

def listar_fichas(procedimentos):
    listas = []
    for proc in procedimentos:
        listas.extend(Ficha_Diagnostico.objects.filter(procedimento=proc))
        listas.extend(Ficha_Ortodontia.objects.filter(procedimento=proc))
        listas.extend(Ficha_Periodontia.objects.filter(procedimento=proc))
        listas.extend(Ficha_Urgencia.objects.filter(procedimento=proc))
        listas.extend(Ficha_Endodontia.objects.filter(procedimento=proc))
        listas.extend(Ficha_Endodontia_Tabela.objects.filter(procedimento=proc))
        listas.extend(Ficha_PPR.objects.filter(procedimento=proc))
        listas.extend(Ficha_Dentistica.objects.filter(procedimento=proc))
    return listas

#Listar as fichas do paciente com base no CPF 
#Fluxo: buscar_paciente
#Action: listar_fichas_paciente 
@login_required
def buscar_fichas_paciente(request):
    cpf_p = request.session['cpf_p']
    procedimentos = Procedimento.objects.filter(cpf_p=cpf_p)
    listas = listar_fichas(procedimentos)
    return render(request, 'sistema_fichas/listar_fichas.html', 
                  {'fichas': listas})

@login_required
def detalhar_ficha(request,slug,pk):
    if slug == "diagnostico":
        ficha = get_object_or_404(Ficha_Diagnostico, pk=pk)
        ficha_form = Ficha_DiagnosticoForm(instance = ficha)
    elif slug == "ortodontia":
        ficha = get_object_or_404(Ficha_Ortodontia, pk=pk)
        ficha_form = Ficha_OrtodontiaForm(instance = ficha)
    elif slug == "periodontia":
        ficha = get_object_or_404(Ficha_Periodontia, pk=pk)
        ficha_form = Ficha_PeriodontiaForm(instance = ficha)
    elif slug == "urgencia":
        ficha = get_object_or_404(Ficha_Urgencia, pk=pk)
        ficha_form = Ficha_UrgenciaForm(instance = ficha)
    elif slug == "endodontia":
        ficha = get_object_or_404(Ficha_Endodontia, pk=pk)
        ficha_form = Ficha_EndodontiaForm(instance = ficha)
    elif slug == "endodontia-tabela":
        ficha = get_object_or_404(Ficha_Endodontia_Tabela, pk=pk)
        ficha_form = Ficha_Endodontia_TabelaForm(instance = ficha)
    elif slug == "ppr":
        ficha = get_object_or_404(Ficha_PPR, pk=pk)
        ficha_form = Ficha_PPRForm(instance = ficha)
    elif slug == "dentistica":
        ficha = get_object_or_404(Ficha_Dentistica, pk=pk)
        ficha_form = Ficha_DentisticaForm(instance = ficha)
    return render(request, 'sistema_fichas/detalhar_ficha.html', {'ficha': ficha_form,})

def listar_exames(request):
    cpf_p = request.session['cpf_p']
    paciente = Paciente.objects.get(cpf = cpf_p)
    exames = Exame.objects.filter(cpf_p=cpf_p)
    termo = paciente.termo_cons
    if request.method == 'POST':
        paciente.termo_cons = request.FILES['termo']
        paciente.save()
    return render(request, 'sistema_fichas/listar_exames.html', 
                  {'exames': exames, 'termo': termo})

def cadastrar_planejamento(request):
    if request.method == 'GET':
        formPlan = PlanejamentoForm()
    elif request.method == 'POST':
        cpf_p = request.session['cpf_p']
        paciente = Paciente.objects.get(cpf=cpf_p)
        parc_plan = Planejamento(cpf_p = paciente)
        plan = PlanejamentoForm(request.POST, instance = parc_plan)
        if plan.is_valid():
            parc_plan.save()
            return HttpResponseRedirect(reverse('sistema_fichas:listar_planejamentos'))
    return render(request, 'sistema_fichas/cadastrar_planejamento.html', {'form': formPlan})

def listar_planejamentos(request):
    planejamentos = Planejamento.objects.filter(cpf_p = request.session['cpf_p'])
    return render(request, 'sistema_fichas/listar_planejamentos.html', {'planejamentos': planejamentos})

@login_required
def urgencia(request):
    if request.method == 'POST':
        ficha_form = Ficha_UrgenciaForm(data=request.POST)
        if ficha_form.is_valid():
            ficha = ficha_form.save(commit=False)
            ficha.procedimento = Procedimento.objects.get(pk=request.session['procedimento'])
            ficha.save()
            return redirect('sistema_fichas:listar_procedimentos')
    else:
        ficha_form = Ficha_UrgenciaForm()
    return render(request, 'sistema_fichas/urgencia.html',
                  {'ficha_form': ficha_form})

@login_required
def ppr(request):
    if request.method == 'POST':
        ficha_form = Ficha_PPRForm(request.POST)
        if ficha_form.is_valid():
            ficha = ficha_form.save(commit=False)
            ficha.procedimento = Procedimento.objects.get(pk=request.session['procedimento'])
            ficha.save()
            return redirect('sistema_fichas:listar_procedimentos')
    else:
        ficha_form = Ficha_PPRForm()
    return render(request, 'sistema_fichas/ppr.html',
                  {'ficha_form': ficha_form})

@login_required
def dentistica(request):
    if request.method == 'POST':
        ficha_form = Ficha_DentisticaForm(request.POST)
        if ficha_form.is_valid():
            ficha = ficha_form.save(commit=False)
            ficha.procedimento = Procedimento.objects.get(pk=request.session['procedimento'])
            ficha.save()
            return redirect('sistema_fichas:listar_procedimentos')
    else:
        ficha_form = Ficha_DentisticaForm()
    return render(request, 'sistema_fichas/dentistica.html',
                  {'ficha_form': ficha_form})

@login_required
def odontograma(request):
    if request.method == 'POST':
        ficha_form = OdontogramaForm(request.POST)
        return redirect('sistema_fichas:atendimento_opcoes')
    return render(request, 'sistema_fichas/odontograma2.html')

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

"""
Esta função ainda não foi completada
"""
@login_required
def periodontia(request):
    if request.method == 'POST':
        ficha_form = Ficha_PeriodontiaForm(request.POST)
        if ficha_form.is_valid():
            ficha = ficha_form.save(commit=False)
            ficha.procedimento = Procedimento.objects.get(pk=request.session['procedimento'])
            ficha.save()
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




#Histórico da ficha específica na turma selecionada
#Fluxo: detalhar_turma
#Action: historico_fichapass
@login_required
def historico_fichas_turma(request):
    pass

