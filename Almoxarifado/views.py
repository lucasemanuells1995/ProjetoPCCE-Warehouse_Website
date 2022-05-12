from multiprocessing import context
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Pergunta, Alternativa, Descricao


def index(request):
    pergunta_calibre = Pergunta.objects.get(id=1)   #Aqui ele pega no banco de dados a pergunta sobre o calibre
    context = {'pergunta_calibre': pergunta_calibre}
    pergunta_calibre.save()
    return render(request, 'Almoxarifado/index.html')
    
    #Retorna a resposta acima quando views.index for chamado

def calibre(request, pergunta_id):
    p = get_object_or_404(Pergunta, pk=pergunta_id) #Verifica se a pergunta selecionada existe
    try:
        pergunta_selecionada1 = p.alternativa_set.get(pk=request.POST['alternativa']) #Caso sim, mostra as alternativas e pega o id da escolhida
    except KeyError:    #Caso não selecione uma alternativa, avisa que nenhuma alternativa foi selecionada
        return render(request, 'Almoxarifado/calibre.html',
            {'pergunta': pergunta,
            'error_message': "Você não selecionou uma alternativa.",
            })
    else:               #Caso selecione, salva o id da alternativa, e indica o caminho para a segunda pergunta
        pergunta_selecionada1.save()
        p1 = pergunta_selecionada1.id
        pergunta_calibre = Pergunta.objects.get(id=2)
        return render(request, 'Almoxarifado/objeto.html')


def objeto(request):
    p = get_object_or_404(Pergunta, pk=pergunta_id) #Verifica se a pergunta selecionada existe
    try:
        pergunta_selecionada2 = p.alternativa_set.get(pk=request.POST['alternativa']) #Caso sim, mostra as alternativas e pega o id da escolhida
    except KeyError:    #Caso não selecione uma alternativa, avisa que nenhuma alternativa foi selecionada
        return render(request, 'Almoxarifado/objeto.html',
            {'pergunta': pergunta,
            'error_message': "Você não selecionou uma alternativa.",
            })
    else:               #Caso selecione, salva o id da alternativa, e indica o caminho para a segunda pergunta
        pergunta_selecionada2.save()
        p2 = pergunta_selecionada2.id
        pergunta_calibre = Pergunta.objects.get(id=3)
        return render(request, 'Almoxarifado/arma.html')

def arma(request):
    p = get_object_or_404(Pergunta, pk=pergunta_id) #Verifica se a pergunta selecionada existe
    try:
        pergunta_selecionada3 = p.descricao_set.get(pk=request.POST['descricao']) #Caso sim, mostra as alternativas e pega o id da escolhida
    except KeyError:    #Caso não selecione uma alternativa, avisa que nenhuma alternativa foi selecionada
        return render(request, 'Almoxarifado/arma.html',
            {'pergunta': pergunta,})

    else:               #Caso selecione, salva o id da alternativa, e indica o caminho para a segunda pergunta
        pergunta_selecionada3.save()
        p3 = pergunta_selecionada3.id
        pergunta_calibre = Pergunta.objects.get(id=4)
        return render(request, 'Almoxarifado/municao.html')

def municao(request):
    p = get_object_or_404(Pergunta, pk=pergunta_id) #Verifica se a pergunta selecionada existe
    try:
        pergunta_selecionada4 = p.descricao2_set.get(pk=request.POST['descricao2']) #Caso sim, mostra as alternativas e pega o id da escolhida
    except KeyError:    #Caso não selecione uma alternativa, avisa que nenhuma alternativa foi selecionada
        return render(request, 'Almoxarifado/municao.html',
            {'pergunta': pergunta,})

    else:               #Caso selecione, salva o id da alternativa, e indica o caminho para a segunda pergunta
        pergunta_selecionada4.save()
        p4 = pergunta_selecionada4.id
        pergunta_calibre = Pergunta.objects.get(id=1)
        return render(request, 'Almoxarifado/municao.html')
