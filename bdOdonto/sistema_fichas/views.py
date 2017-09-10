from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import *
from .forms import *

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
def odontograma(request):
    return render(request, 'sistema_fichas/odontograma.html')

@login_required
def user_logout(request):
    logout(request)
    if request.session.has_key('turma_atual'):
        del request.session['turma_atual']
    return HttpResponseRedirect('/accounts/login')
	
def registrar_usuario(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        aluno_form = AlunoForm(data=request.POST)
        if user_form.is_valid() and aluno_form.is_valid():
            user = user_form.save(commit=False)
            user.set_password(user.password)
            user.save()
            aluno = aluno_form.save(commit=False)
            aluno.usuario = user
            aluno.save()
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

def verify_url(nome_ficha):
    if nome_ficha == "Ficha Diagnostico":
        return "sistema_fichas/ficha_diagnostico.html"
    elif nome_ficha == "Ficha Ortodontia":
        return "sistema_fichas/ficha_ortodontia.html"
    elif nome_ficha == "Ficha Periodontia":
        return "sistema_fichas/ficha_periodontia.html"
    elif nome_ficha == "Ficha Urgencia":
        return "sistema_fichas/ficha_urgencia.html"
    elif nome_ficha == "Ficha Endodontia":
        return "sistema_fichas/ficha_endodontia.html"
    elif nome_ficha == "Ficha Endodontia Tabela":
        return "sistema_fichas/ficha_endodontia_tabela.html"
    elif nome_ficha == "Ficha PPR":
        return "sistema_fichas/ficha_ppr.html"
    elif nome_ficha == "Ficha Dentistica":
        return "sistema_fichas/ficha_dentistica.html"
    else:
        return None

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
    url = verify_url(ficha.nome)
    request.session['ficha_atual'] = ficha.codigo
    request.session.modified = True
    t_codigo = request.session['turma_atual']
    turma = get_object_or_404(Turma, codigo=t_codigo)
    aluno = get_object_or_404(Aluno, usuario=request.user)
    usuario = aluno.usuario
    return render(request, 'sistema_fichas/info_ficha.html',
                  {'ficha' : ficha,
                   'turma': turma,
                   'aluno': usuario})

@login_required
def atendimento(request):
    if request.method == 'POST':
        aluno = Aluno.objects.filter(usuario=request.user)
        turma = request.session['turma_atual']
        turma_aluno = get_object_or_404(Turma_Aluno, turma=turma, aluno=aluno)
        ficha = get_object_or_404(Tipo_Ficha, pk=request.session['ficha_atual'])
        atendimento_form = AtendimentoForm(request.POST)
        paciente_form = PacienteForm(request.POST)
        if paciente_form.is_valid() and atendimento_form.is_valid():
            paciente = paciente_form.save(commit=False)
            paciente.turma_aluno = turma_aluno
            paciente.save()
            atendimento = atendimento_form.save(commit=False)
            atendimento.data = timezone.now()
            atendimento.turma_aluno = turma_aluno
            atendimento.tipo_ficha = ficha
            atendimento.paciente = paciente
            atendimento.save()
        else:
            raise ValidationError('Username with tath email or password'
                                  + 'already exists')
    else:
        atendimento_form = AtendimentoForm()
        paciente_form = PacienteForm()
    return render(request, 'sistema_fichas/atendimento.html',
                  {'atendimento_form': atendimento_form,
                   'paciente_form': paciente_form})
