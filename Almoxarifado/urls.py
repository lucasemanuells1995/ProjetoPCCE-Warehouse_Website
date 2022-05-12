from django.urls import path
from . import views
import Almoxarifado

app_name = 'almoxarifado'

urlpatterns = [
    path('', views.index, name='index'),    #Define padrão de URL para cada view.
    path('<int:question_id>/calibre/', views.calibre, name='calibre'),
    path('<int:question_id>/objeto/', views.objeto, name='objeto'),
    path('<int:question_id>/arma/', views.arma, name='arma'),
    path('<int:question_id>/municao/', views.municao, name='municao'),
]