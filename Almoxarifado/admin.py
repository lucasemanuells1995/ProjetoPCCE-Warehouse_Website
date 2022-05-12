from django.contrib import admin

#No site/admin Consigo ver, alterar, adicionar, etc. perguntas e alternativas
from .models import Pergunta, Alternativa, Descricao, Descricao2

admin.site.register(Pergunta)
admin.site.register(Alternativa)
admin.site.register(Descricao)
admin.site.register(Descricao2)

