from django.shortcuts import render, get_object_or_404

def lista_fichas_axluno(request):
    if request.method == 'POST':
        requested_aluno = get_object_or_404(Aluno, pk=request.POST['aluno_mat'])
	requested_turma = get_object_or_404(Turma, pk=request.POST['turma_code'])
	requested_rela = get_object_or_404(Turma_Aluno, turma=requested_turma, aluno=requested_aluno, periodo=request.POST['periodo'])
	requested_atendimentos = Atendimentos.objects.find(turma_aluno = requested_rela)
	ficha_lista = list()
	for atendi in requested_atendimentos:
		if atendi.tipo_ficha == 1:
			ficha_lista.append(get_object_or_404(Ficha_Diagnostico, codeA=atendi.code))	
		elif:
			pass
	return render(request, 'lista_fichas_aluno.html', {'fichas': ficha_lista})

def odontograma(request):
    return render(request, 'odontograma.html')
