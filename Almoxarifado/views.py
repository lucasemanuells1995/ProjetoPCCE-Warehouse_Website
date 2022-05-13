from multiprocessing import context
from re import I
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from .models import Pergunta, Alternativa, Descricao

pergunta_calibre = Pergunta.objects.filter(texto='1. Qual calibre você quer escolher?')   #Aqui ele pega no banco de dados a pergunta sobre o calibre
pergunta_selecionada1 = 0

def index(request):
    return render(request, 'Almoxarifado/index.html', {'pergunta_calibre': pergunta_calibre})
    
    #Retorna a resposta acima quando views.index for chamado

def calibre(request, pergunta_id):
    global pergunta_selecionada1
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id) #Verifica se a pergunta selecionada existe
    try:
        pergunta_selecionada1 = pergunta.alternativa_set.get(pk=request.POST['alternativa']) #Caso sim, mostra as alternativas e pega o id da escolhida
    except KeyError:    #Caso não selecione uma alternativa, avisa que nenhuma alternativa foi selecionada
        return render(request, 'Almoxarifado/calibre.html' ,
        {'pergunta': pergunta,
        'error_message': "Selecione uma alternativa.",})
    else:               #Caso selecione, salva o id da alternativa, e indica o caminho para a segunda pergunta
        pergunta_calibre = Pergunta.objects.filter(texto='2. É arma ou munição?')
        pergunta_selecionada1 = pergunta_selecionada1.pk
    return render(request, 'Almoxarifado/index2.html', {'pergunta_calibre': pergunta_calibre})

def index2(request):
    return render(request, 'Almoxarifado/index2.html', {'pergunta_calibre': pergunta_calibre})

    #Retorna a resposta acima quando views.index2 for chamado

def objeto(request, pergunta_id):
    pergunta = get_object_or_404(Pergunta, pk=pergunta_id) #Verifica se a pergunta selecionada existe
    try:
        pergunta_selecionada2 = pergunta.alternativa_set.get(pk=request.POST['alternativa']) #Caso sim, mostra as alternativas e pega o id da escolhida
    except KeyError:    #Caso não selecione uma alternativa, avisa que nenhuma alternativa foi selecionada
        return render(request, 'Almoxarifado/objeto.html' ,
        {'pergunta': pergunta,
        'error_message': "Selecione uma alternativa.",})
    else:               #Caso selecione, salva o id da alternativa, e indica o caminho para a segunda pergunta
        
        pergunta_calibre = Pergunta.objects.filter(texto='Arma')
    return render(request, 'Almoxarifado/indexarma.html', {'pergunta_calibre': pergunta_calibre})

def indexarma(request):
    return render(request, 'Almoxarifado/indexarma.html', {'pergunta_calibre': pergunta_calibre})

def arma(request, pergunta_id):
    global pergunta_selecionada1
    if get_object_or_404(Pergunta, pk=pergunta_id): #Verifica se foi selecionado arma

        pergunta_calibre = Pergunta.objects.filter(texto='Munição')
        desc = Descricao.objects.filter(id=pergunta_selecionada1)
        return render(request, 'Almoxarifado/arma.html', {'pergunta_calibre': pergunta_calibre, 'desc': desc})
    else:               #Caso selecione, salva o id da alternativa, e indica o caminho para a segunda pergunta
        return render(request, 'Almoxarifado/arma.html', {'error_message': "Você escolheu Munição.",})
        

def municao(request, pergunta_id):
    global pergunta_selecionada1
    if get_object_or_404(Pergunta, pk=pergunta_id): #Verifica se foi selecionado munição

        pergunta_calibre = Pergunta.objects.filter(texto='Arma')
        desc = Descricao.objects.filter(id=pergunta_selecionada1)
        return render(request, 'Almoxarifado/municao.html', {'pergunta_calibre': pergunta_calibre, 'desc': desc})
    else:               #Caso selecione, salva o id da alternativa, e indica o caminho para a segunda pergunta
        return render(request, 'Almoxarifado/municao.html', {'error_message': "Você escolheu Arma",})