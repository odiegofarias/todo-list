from django.test import TestCase
from django.urls import reverse, resolve
from tarefa import views


class TestViewIndex(TestCase):
    def test_index_view_retorna_status_200(self):
        resposta = self.client.get(reverse('tarefa:index'))
        self.assertEqual(resposta.status_code, 200)

    
    def test_index_view_esta_usando_o_template_correto(self):
        resposta = self.client.get(reverse('tarefa:index'))
        self.assertTemplateUsed(resposta, 'tarefa/index.html')
    
    def test_index_view_index_de_tarefa_esta_correta(self):
        view = resolve(reverse('tarefa:index'))
        self.assertIs(view.func, views.index)

    

    