from django.urls import path

from Almoxarifado.models import Pergunta
from . import views
import Almoxarifado

app_name = 'almoxarifado'

urlpatterns = [
    path('', views.index, name='index'),    #Define padrão de URL para cada view.
    path('<int:pergunta_id>/calibre/', views.calibre, name='calibre'),
    path('<int:pergunta_id>/objeto/', views.objeto, name='objeto'),
    path('<int:pergunta_id>/arma/', views.arma, name='arma'),
    path('<int:pergunta_id>/municao/', views.municao, name='municao'),
]