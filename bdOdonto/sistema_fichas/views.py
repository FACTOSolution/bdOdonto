from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
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

    return HttpResponseRedirect('/accounts/login')

def registrar_usuario(request):
    registered = False
	
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        aluno_form = AlunoForm(data=request.POST)
        if user_form.is_valid() and aluno_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            aluno = aluno_form.save(commit=False)
            aluno.user = user
            aluno.save()
            registered = True
    else:
        user_form = UserForm()
        aluno_form = AlunoForm()
	
    return render(request, 'sistema_fichas/registrar_usuario.html',
                  {'user_form': user_form,
                   'aluno_form': aluno_form,
                   'registered': registered})
