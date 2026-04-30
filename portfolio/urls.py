from django.urls import path
from . import views

urlpatterns = [
    path('', views.tecnologias_view),
    path('docentes/', views.docentes_view, name='docentes'),
    path('licenciaturas/', views.licenciaturas_view, name='licenciaturas'),
    path('unidades-curriculares/', views.unidades_curriculares_view, name='unidades_curriculares'),
    path('tecnologias/', views.tecnologias_view, name='tecnologias'),
    path('projetos/', views.projetos_view, name='projetos'),
    path('tfcs/', views.tfcs_view, name='tfcs'),
    path('competencias/', views.competencias_view, name='competencias'),
    path('formacoes/', views.formacoes_view, name='formacoes'),
    path('makingof/', views.makingof_view, name='makingof'),
    path('conquistas/', views.conquistas_view, name='conquistas'),
]