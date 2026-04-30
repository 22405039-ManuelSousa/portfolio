from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from .models import (Docente, Licenciatura, UnidadeCurricular, Tecnologia,
                     Projeto, TFC, Competencia, Formacao, MakingOf, Conquista)

def docentes_view(request):
    docentes = Docente.objects.all()
    return render(request, 'docentes.html', {'docentes': docentes})

def licenciaturas_view(request):
    licenciaturas = Licenciatura.objects.all()
    return render(request, 'licenciaturas.html', {'licenciaturas': licenciaturas})

def unidades_curriculares_view(request):
    ucs = UnidadeCurricular.objects.select_related('licenciatura').prefetch_related('docentes').all()
    return render(request, 'unidades_curriculares.html', {'ucs': ucs})

def tecnologias_view(request):
    tecnologias = Tecnologia.objects.all()
    return render(request, 'tecnologias.html', {'tecnologias': tecnologias})

def projetos_view(request):
    projetos = Projeto.objects.select_related('unidade_curricular').prefetch_related('tecnologias').all()
    return render(request, 'projetos.html', {'projetos': projetos})

def tfcs_view(request):
    tfcs = TFC.objects.select_related('licenciatura').prefetch_related('tecnologias').all()
    return render(request, 'tfcs.html', {'tfcs': tfcs})

def competencias_view(request):
    competencias = Competencia.objects.prefetch_related('tecnologias', 'projetos').all()
    return render(request, 'competencias.html', {'competencias': competencias})

def formacoes_view(request):
    formacoes = Formacao.objects.prefetch_related('tecnologias', 'competencias').all()
    return render(request, 'formacoes.html', {'formacoes': formacoes})

def makingof_view(request):
    makingof = MakingOf.objects.select_related('projeto', 'tecnologia', 'unidade_curricular').all()
    return render(request, 'makingof.html', {'makingof': makingof})

def conquistas_view(request):
    conquistas = Conquista.objects.prefetch_related('projetos', 'tecnologias').all()
    return render(request, 'conquistas.html', {'conquistas': conquistas})