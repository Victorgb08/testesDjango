from django.http import JsonResponse
from .models import Livro

def lista_livros(request):
    livros = Livro.objects.all()
    data = [{"titulo": l.titulo, "autor": l.autor, "ano": l.ano_publicacao} for l in livros]
    return JsonResponse({"livros": data})
