# -*- coding: utf-8 -*-
from django.views import  View
from django.views.generic import  ListView, DetailView, TemplateView
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import logout, authenticate
from django.contrib.auth.models import User
from django.contrib import auth
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.decorators import method_decorator
from django.core.exceptions import ValidationError
from django.http import HttpResponseRedirect
from django.urls import reverse
from .models import *
from .forms import *


############################################# REDIRECIONAMENTO (TALVEZ) ############################
def usuario_prof(user, request):
    """
    SUJEITA A ALTERAÇÕES.
    Essa função verifica se existe um usuário logado e se ele é um professor.
    Ela é usada para impedir o acesso de usuários não autorizados a funcionalidades que apenas um professor deve ter acesso
    """
    if request.user.is_authenticated:       #Verifica se existe um usuário logado na função
        try:
            Professor.objects.get(usuario = user)
        except Professor.DoesNotExist:      #Se o usuário logado não estiver na tabela professor, significa que ele não deve ter acesso, então retorna-se False
            return False
    else:                                   #Se o usuário não está logado
        return False
    return True

def login(request):
    """
    Responsável por logar o usuário na sessão.
    """
    if request.method == 'POST':    
        #form = AuthenticationForm(data=request.POST) # Veja a documentacao desta funcao
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)       #Tenta autenticar o os dados passado. Se o usuário não for autenticado, retorna-se None

        if user is not None:                #se existe um usuário no BD com os dados passados
            auth.login(request, user)       #registra ele na tabela auth do django
            if usuario_prof(user, request):         #Verifica se o usuário é professor e o leva para a tela de listagem de turmas
                return HttpResponseRedirect('listar_turmas') # redireciona o usuario logado para a pagina inicial
            else:
                return HttpResponseRedirect('buscar_paciente') # redireciona o usuario aluno logado para a pagina inicial
        else:
            return render(request, "registration/login.html", {'err': True})
    
    #se nenhuma informacao for passada, exibe a pagina de login com o formulario
    return render(request, "registration/login.html", {})

@login_required
def user_logout(request):
    """
    Responsável por deslogar o usuário
    """
    logout(request)
    if request.session.has_key('turma_atual'):
        del request.session['turma_atual']
    return HttpResponseRedirect(reverse('sistema_fichas:login'))

@method_decorator(login_required, name='dispatch')
class BuscarPacienteView(View):
    """
    Classe responsável por fazer a busca por pacientes no banco de dados.
    """
    def get(self, request):
        """
        Retorna o Template de busca a um usuário
        """
        username = request.user.username
        return render(request, 'sistema_fichas/buscar_paciente.html', {'username': username})
    
    def post(self, request):
        """
        Busca por um paciente a partir do CPF passado, levando ao prontuário do paciente caso ele exista ou permitindo a criação de um novo paciente
        """
        cpf_p = request.POST['cpf_p']
        request.session['cpf_p'] = cpf_p
        try:
            Paciente.objects.get(pk=cpf_p)
            return HttpResponseRedirect(reverse('sistema_fichas:menu_paciente'))
        except Paciente.DoesNotExist:
            return render(request, 'sistema_fichas/paciente_nao_encontrado.html',  {'cpf': cpf_p})

@method_decorator(login_required, name='dispatch')
class MenuPacienteView(TemplateView):
    """
    Resposável por exibir o prontuário do paciente
    """
    template_name = 'sistema_fichas/menu_paciente.html'         #A página que mostra os dados do prontuário do Paciente

    def get_context_data(self):                                         #Metodo da classe super TemplateView. Busca o conteúdo que deverá ser exibido no template
        context = super(MenuPacienteView, self).get_context_data()      #captura o contexto disponibilizado na classe TemplateView. Necessária.
        cpf_p = self.request.session.get('cpf_p', None)                 #salva o cpf do paciente da sessão
        paciente = Paciente.objects.get(pk=cpf_p)                       #recupera o objeto Paciente do banco de dados
        qt_procedimentos = len(Procedimento.objects.filter(cpf_p=paciente.cpf))     #verifica a quantidade de procedimentos em nome do Paciente
        context['paciente'] = paciente                                  #insere o paciente recuperado no contexto que será retornado ao template
        context['qt_procedimentos'] = qt_procedimentos                  #insere o a quantidade de procedimentos no contexto que será retornado ao template
        return context                                      #retorna o contexto para a renderização

@login_required
def opcoes_ficha(request, slug):
    """
    Essa função é resposável por limitar as fichas que podem ser cadastradas de acordo
    com a matéria declarada no preenchimento do Procedimento
    """
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

############################################# CADASTRO #############################################
@method_decorator(login_required, name='dispatch')
class CadastroView(View):
    """
    Classe Pai para as demais classes de cadastro. Essa classe contêm apenas o trecho de código em comum entre as classes.
    Cada classe que deriva esta implementa seu próprio método post. O método get é comum para todas as classes.
    """
    form_class = None           #Essas são variáveis comuns às demais classes filhas, e cada classe filha a modifica de acordo com sua necessidade. Form_class é a tipo do formulário que deverá ser retornado em cada situação.
    template_get_nome = None    #O template que deve ser retornado ao chamar o método get de cada classe filha.
    template_post_nome = None   #O template que deve ser retornado ao chamar o método post de cada classe filha.

    def get(self, request, *args, **kwargs):    #Similar à implementação na forma 'if request.method == 'GET', porém esta implementação permite o reaproveitamento de código
        form = self.form_class()                #instancia o objeto formulário adequado a cada situação
        return render(request, self.template_get_nome, {'form': form})      #retorna a o template adequado para cada classe filha
    
    def post(self, request, form):
        if form.is_valid():     #verifica a validade do formulário
            form.save()         #salva o objeto que preenche o formulário validado diretamento no banco de dados
            return HttpResponseRedirect(reverse(self.template_post_nome))       #Encaminha a página devida em cada situação.
        else:
            return render(request, self.template_get_nome, {'form':self.form_class})    #caso o formulário seja inválido, o usuário é levado de volta a página de preenchimento do formulário

class CadastrarPaciente(CadastroView):
    """
    CLASSE FILHA DE CadastroView.
    Opera os métodos GET e POST de um formulário responsável por criar um novo paciente
    """
    form_class = PacienteForm       #'PacienteForm' é o formulário que representa as informações de um paciente. Esse formulário será renderizado no template HTML.
    template_get_nome = 'sistema_fichas/cadastrar_paciente.html'    #o template HTML que representa a função de criar um novo paciente.
    template_post_nome = 'sistema_fichas:menu_paciente'             #o template HTML que será retornado após o post(criação) de um novo paciente.
    
    def post(self, request, *args, **kwargs): 
        """
        Método que será chamado quando o usuário fizer o upload das informações de um novo paciente.
        """  
        formPaciente = PacienteForm(request.POST, request.FILES)    #povoa um formulário de paciente com as informações inseridas no <form> do HTML.
        return super().post(request,formPaciente)                   #chama o método post da classe pai(CadastroView) passando o formulário que deverá ser validado e que poderá salvar um novo objeto no BD.

class CadastrarPlanejamento(CadastroView):
    """
    CLASSE FILHA DE CadastroView.
    Opera os métodos GET e POST de um formulário responsável por criar um novo Planejamento.
    """
    form_class = PlanejamentoForm   #'PlanejamentoForm' é o formulário que representa as informações de um planejamento. Esse formulário será renderizado no template HTML.
    template_get_nome = 'sistema_fichas/cadastrar_planejamento.html'    #o template HTML que representa a função de criar um novo planejamento.
    template_post_nome = 'sistema_fichas:listar_planejamentos'          #o template HTML que será retornado após o post(criação) de um novo planejamento.
    
    def post(self, request, *args, **kwargs):
        """
        Método que será chamado quando o usuário fizer o upload das informações de um novo planejamento.
        """  
        cpf_p = request.session['cpf_p']                #resgata o cpf do paciente inserido na sessão(Ver a função buscar_paciente).
        paciente = Paciente.objects.get(pk=cpf_p)       #resgata o objeto Paciente com o cpf da sessão.
        parc_plan = Planejamento(cpf_p = paciente)      #cria um objeto planejamento parcialmente preenchido. Esse objeto será usado abaixo para povoar o formulário.
        plan = PlanejamentoForm(request.POST, instance = parc_plan)     #povoa um formulário de planejamento com as informações inseridas no <form> do HTML.
        return super().post(request,plan)               #chama o método post da classe pai(CadastroView) passando o formulário que deverá ser validado e que poderá salvar um novo objeto no BD.

class CadastrarProcedimento(CadastroView):
    """
    CLASSE FILHA DE CadastroView.
    Opera os métodos GET e POST de um formulário responsável por criar um novo Procedimento.
    """
    form_class = ProcedimentoForm           #'ProcedimentoForm' é o formulário que representa as informações de um Procedimento. Esse formulário será renderizado no template HTML.
    template_get_nome = 'sistema_fichas/cadastrar_procedimento.html'    #o template HTML que representa a função de criar um novo Procedimento.
    template_post_nome = 'sistema_fichas:listar_procedimento'          #o template HTML que será retornado após o post(criação) de um novo Procedimento.

    def post(self, request, *args, **kwargs):
        cpf_p = request.session['cpf_p']
        paciente = Paciente.objects.get(pk=cpf_p)
        
        parc_procedimento = Procedimento(cpf_p = paciente)
        formProcedimento = ProcedimentoForm(request.POST, request.FILES, instance=parc_procedimento)
        parc_procedimento = formProcedimento.save(commit=False)
        turma = parc_procedimento.tap.turma

        if formProcedimento.is_valid():
            request.session['proc_descricao'], request.session['proc_tap'] = parc_procedimento.descricao, parc_procedimento.tap.id
            if formProcedimento.cleaned_data['exame']:
                if len(request.FILES) != 0:
                    imagem = request.FILES['exame_img']
                    parc_exame = Exame(cpf_p = paciente, imagem=imagem)
                    parc_exame.save()
                    request.session['proc_exame'] = 1
                else:
                    return render(request, 'sistema_fichas/cadastrar_procedimento.html', {'form': formProcedimento, 'err_upload': True})
            else:
                request.session['proc_exame'] = 0
            if formProcedimento.cleaned_data['ficha_ou_procedimento']:
                materia = turma.replace(" ", "")
                return HttpResponseRedirect(reverse('sistema_fichas:opcoes_ficha', args=(materia,)))
            return HttpResponseRedirect(reverse('sistema_fichas:listar_procedimentos'))
        else:
            return render(request, self.template_get_nome, {'form':self.form_class})

############################################# LISTAGEM #############################################
"""
O código escrito pra funcionalidade de listar objetos se alterna entre classes e funções.
Algumas views em forma de função foram mantidas pois ficaram mais intendíveis e requeriram menos código do que se fossem implementadas em classes.
As classes implementam a classe ListView, disponibilizada pelo próprio Django.
"""

@method_decorator(login_required, name='dispatch')
class ListarFichasView(ListView):
    """
    Essa classe retorna as fichas de um paciente.
    """
    template_name = 'sistema_fichas/listar_fichas.html'     #o template que rederizará as informações de fichas obtidas.
    model = Paciente                                        #Variável padrão e obrigatória da classe ListView.

    def get_context_data(self):                 #Essa função é resposável por implementar a lógica da busca pelos objetos desejados em cada classe.
        cpf_p = self.request.session['cpf_p']   #resgata o cpf do paciente inserido na sessão(Ver a função buscar_paciente).
        procedimentos = Procedimento.objects.filter(cpf_p=cpf_p)    #Como cada ficha é ligada a um procedimento, é necessária a lista de procedimentos para que as fichas sejam identificadas.
        fichas = []
        for proc in procedimentos:          #Com a chave primária que identifica cada procedimento, é feita a busca em todas as tabelas de fichas por fichas que tenham como chave secundária o procedimento em questão.
            fichas.extend(Ficha_Diagnostico.objects.filter(procedimento=proc))
            fichas.extend(Ficha_Ortodontia.objects.filter(procedimento=proc))
            fichas.extend(Ficha_Periodontia.objects.filter(procedimento=proc))
            fichas.extend(Ficha_Urgencia.objects.filter(procedimento=proc))
            fichas.extend(Ficha_Endodontia.objects.filter(procedimento=proc))
            fichas.extend(Ficha_Endodontia_Tabela.objects.filter(procedimento=proc))
            fichas.extend(Ficha_PPR.objects.filter(procedimento=proc))
            fichas.extend(Ficha_Dentistica.objects.filter(procedimento=proc))
        context = super(ListarFichasView, self).get_context_data()      #esse método será repetido as demais classes filhas. Ele pega a variável de contexto da classe ListView(um dicionário) para que depois seja adicionado o contexto capturado.
        context['fichas'] = fichas      #adiciona o contexto criado nesse método ao contexto da classe Pai(ListView) que retornará o template com o contexto adequado.
        return context

class ListarTurmasView(UserPassesTestMixin, ListView):
    model= TAP                                              #Variável padrão e obrigatória da classe ListView.
    template_name = 'sistema_fichas/listar_turmas.html'     #o template que rederizará as informações de Turmas obtidas.

    def test_func(self):
        return usuario_prof(self.request.user, self.request)

    def get_context_data(self):         #Essa função é resposável por implementar a lógica da busca pelos objetos desejados em cada classe.
        context = super(ListarTurmasView, self).get_context_data()      #Pega a variável de contexto da classe ListView(um dicionário) para que depois seja adicionado o contexto aqui criado.
        prof = Professor.objects.get(usuario=self.request.user)         #Retorna o objeto professor apartir do usuário logado na sessão.
        context['turmas'] = TAP.objects.filter(cod_prof=prof.codigo)    #Adiciona as turmas em que o professor está cadastrado ao contexto de ListView.
        return context

@method_decorator(login_required, name='dispatch')
class ListarExamesView(ListView):
    model = Exame                                           #Variável padrão e obrigatória da classe ListView.
    template_name = 'sistema_fichas/listar_exames.html'     #o template que rederizará as informações de Exames obtidos.
    
    def get_context_data(self):         #Essa função é resposável por implementar a lógica da busca pelos objetos desejados em cada classe.
        context = super(ListarExamesView, self).get_context_data()      #Pega a variável de contexto da classe ListView(um dicionário) para que depois seja adicionado o contexto aqui criado.
        cpf_p = self.request.session['cpf_p']               #resgata o cpf do paciente inserido na sessão(Ver a função buscar_paciente).
        exames = Exame.objects.filter(cpf_p=cpf_p)          #Resgata os exames que são relacionados ao paciente a partir do seu CPF.
        context['exames'] = exames                      #Adiciona os Exames capturados ao contexto de ListView.
        return context
      
@login_required
def listar_procedimentos(request):
    """
    Retorna os procedimentos ligados ao paciente pelo seu CPF.
    """
    list_proc = Procedimento.objects.filter(cpf_p = request.session['cpf_p'])
    return render(request, 'sistema_fichas/listar_procedimentos.html', {'procedimentos':list_proc})

@login_required
def listar_planejamentos(request):
    """
    Retorna os planejamentos ligados ao paciente pelo seu CPF.
    """
    planejamentos = Planejamento.objects.filter(cpf_p = request.session['cpf_p'])
    return render(request, 'sistema_fichas/listar_planejamentos.html', {'planejamentos': planejamentos})

############################################# DETALHES #############################################

@login_required
def detalhar_paciente(request):
    """
    Função responsável por detalhar um Paciente.
    """
    cpf_p = request.session['cpf_p']
    paciente = Paciente.objects.get(pk=cpf_p)                       #recupera o objeto Paciente adequado do banco de dados
    formPaciente = PacienteForm(instance=paciente)                  #Cria um formulário que será mostrado no template e o povoa com as informações do Paciente recuperado
    return render(request, 'sistema_fichas/detalhes_paciente.html', {'form': formPaciente})         #Renderiza a página adequada com as informações devidas

@login_required
def detalhar_ficha(request,slug,pk):
    """
    Função responsável por detalhar uma ficha de acordo com o tipo de ficha e a chave primária passada por url.
    """
    if slug == "Diagnóstico":
        ficha = get_object_or_404(Ficha_Diagnostico, pk=pk)
        ficha_form = Ficha_DiagnosticoForm(instance = ficha)
    elif slug == "Ortodontia":
        ficha = get_object_or_404(Ficha_Ortodontia, pk=pk)
        ficha_form = Ficha_OrtodontiaForm(instance = ficha)
    elif slug == "Periodontia":
        ficha = get_object_or_404(Ficha_Periodontia, pk=pk)
        ficha_form = Ficha_PeriodontiaForm(instance = ficha)
    elif slug == "Urgência":
        ficha = get_object_or_404(Ficha_Urgencia, pk=pk)
        ficha_form = Ficha_UrgenciaForm(instance = ficha)
    elif slug == "Endodontia":
        ficha = get_object_or_404(Ficha_Endodontia, pk=pk)
        ficha_form = Ficha_EndodontiaForm(instance = ficha)
    elif slug == "Endodontia-Tabela":
        ficha = get_object_or_404(Ficha_Endodontia_Tabela, pk=pk)
        ficha_form = Ficha_Endodontia_TabelaForm(instance = ficha)
    elif slug == "PPR":
        ficha = get_object_or_404(Ficha_PPR, pk=pk)
        ficha_form = Ficha_PPRForm(instance = ficha)
    elif slug == "Dentistica":
        ficha = get_object_or_404(Ficha_Dentistica, pk=pk)
        ficha_form = Ficha_DentisticaForm(instance = ficha)
    return render(request, 'sistema_fichas/detalhar_ficha.html', {'ficha': ficha_form,})

@login_required
def detalhar_procedimento(request,pk):
    """
    Função responsável por detalhar um planejamento.
    """
    procedimento = get_object_or_404(Procedimento, pk = pk)                     #recupera o objeto Procedimento adequado do banco de dados
    formProcedimento = ProcedimentoForm(instance=procedimento)                  #Cria um formulário que será mostrado no template e o povoa com as informações do Procedimento recuperado
    return render(request, 'sistema_fichas/detalhar_procedimento.html', {'ficha': formProcedimento})    #Renderiza a página adequada com as informações devidas

@login_required
def detalhar_planejamento(request,pk):
    """
    Função responsável por detalhar um planejamento.
    """
    planejamento = get_object_or_404(Planejamento, pk = pk)             #recupera o objeto Planejamento adequado do banco de dados
    formPlan = PlanejamentoForm(instance=planejamento)                  #Cria um formulário que será mostrado no template e o povoa com as informações do Planejamento recuperado
    return render(request, 'sistema_fichas/detalhar_planejamento.html', {'ficha': formPlan})        #Renderiza a página adequada com as informações devidas

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

############################################# FORMULÁRIO ###########################################
@method_decorator(login_required, name='dispatch')
class FichasView(View):
    ficha_Form = None
    template_get_nome = None
    template_post_nome = 'sistema_fichas:listar_procedimentos'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_get_nome, {'ficha_form': self.ficha_Form()})
    
    def post(self, request, *args, **kwargs):
        ficha = self.ficha_Form(request.POST)
        if ficha.is_valid():
            procedimento = Procedimento(descricao = request.session['proc_descricao'], ficha_ou_procedimento = True)
            procedimento.tap = TAP.objects.get(pk=request.session['proc_tap'])
            procedimento.cpf_p = Paciente.objects.get(pk=request.session['cpf_p'])
            procedimento.exame = request.session['proc_exame']
            procedimento.save()
            ficha = ficha.save(commit=False)
            ficha.procedimento = procedimento
            ficha.save()
            return redirect(self.template_post_nome)

class DentisticaView(FichasView):
    ficha_Form = Ficha_DentisticaForm
    template_get_nome = 'sistema_fichas/dentistica.html'

class PPRView(FichasView):
    ficha_Form = Ficha_PPRForm
    template_get_nome = 'sistema_fichas/ppr.html'

class UrgenciaView(FichasView):
    ficha_Form = Ficha_UrgenciaForm
    template_get_nome = 'sistema_fichas/urgencia.html'

@login_required
def odontograma(request):
    if request.method == 'POST':
        ficha_form = OdontogramaForm(request.POST)
        if ficha_form.is_valid():
            ficha = ficha_form.save(commit=False)
            ficha.procedimento = Procedimento.objects.get(pk=request.session['procedimento'])
            ficha.save()
            return redirect('sistema_fichas:listar_procedimentos')
    else:
        return render(request, 'sistema_fichas/odontograma2.html')

    if request.method == 'POST':
        requested_aluno = get_object_or_404(Aluno, pk=request.POST['aluno_mat'])
        requested_turma = get_object_or_404(Turma, pk=request.POST['turma_code'])



"""FUNÇÕES QUE PODEM SER REAPROVEITADAS NA PARTE DO PROFESSOR
@login_required
def lista_fichas_aluno(request):
        requested_rela = get_object_or_404(Turma_Aluno, turma=requested_turma, aluno=requested_aluno, periodo=request.POST['periodo'])
        requested_atendimentos = Atendimento.objects.find(turma_aluno = requested_rela)
        ficha_lista = list()
    for atendi in requested_atendimentos:
        if atendi.tipo_ficha == 1:
            ficha_lista.append(get_object_or_404(Ficha_Diagnostico, codeA=atendi.code))
        else:
            pass
    return render(request, 'lista_fichas_aluno.html', {'fichas': ficha_lista})

def registrar_usuario(request):
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
                   'aluno_form': aluno_form})

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

"""