from django.test import TestCase, Client
from django.core.exceptions import ValidationError
from .models import Livro

class LivroModelTest(TestCase):
    def test_criacao_valida(self):
        livro = Livro.objects.create(titulo="Dom Casmurro", autor="Machado de Assis", ano_publicacao=1899)
        self.assertTrue(isinstance(livro, Livro))
        self.assertEqual(str(livro), "Dom Casmurro (1899) por Machado de Assis")

    def test_ano_invalido(self):
        with self.assertRaises(ValidationError):
            livro = Livro(titulo="Futuro Livro", autor="Autor", ano_publicacao=3000)
            livro.full_clean()  # Executa validações

class LivroViewTest(TestCase):
    def setUp(self):
        Livro.objects.create(titulo="O Hobbit", autor="Tolkien", ano_publicacao=1937)

    def test_resposta_livros(self):
        client = Client()
        response = client.get("/livros/")
        self.assertEqual(response.status_code, 200)
        self.assertIn("O Hobbit", response.content.decode())

    def test_view_sem_livros(self):
        Livro.objects.all().delete()
        client = Client()
        response = client.get("/livros/")
        self.assertContains(response, "livros", status_code=200)
