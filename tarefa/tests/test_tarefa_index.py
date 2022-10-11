from django.test import TestCase
from django.urls import reverse, resolve
from tarefa import views
from tarefa.models import Tarefa
from parameterized import parameterized


class TarefaTestBase(TestCase):
    def setUp(self):
        return super().setUp()

    def criar_tarefa(self, nome = 'tarefa teste', feita = False, data_criacao = None):
        return Tarefa.objects.create(
            nome=nome,
            feita=feita,
            data_criacao=data_criacao
        )
    

class TestViewIndex(TarefaTestBase):
    def test_index_view_retorna_status_200(self):
        resposta = self.client.get(reverse('tarefa:index'))
        self.assertEqual(resposta.status_code, 200)

    
    def test_index_view_esta_usando_o_template_correto(self):
        resposta = self.client.get(reverse('tarefa:index'))
        self.assertTemplateUsed(resposta, 'tarefa/list.html')
    
    def test_index_view_de_tarefa_esta_correta(self):
        view = resolve(reverse('tarefa:index'))
        self.assertIs(view.func, views.index)

    def test_tarefa_index_carrega_tarefas(self):
        self.criar_tarefa(
            nome="Estudar Testes com Django",
        )
        resp = self.client.get(reverse('tarefa:index'))
        content = resp.content.decode('UTF-8')
        self.assertIn('Estudar Testes com Django', content)
        

    def test_template_list_coloca_atributo_html_strike_nas_tarefas_feitas_True(self):
        self.criar_tarefa(
            feita=True,
        )
        resp = self.client.get(reverse('tarefa:index'))
        content = resp.content.decode('UTF-8')
        self.assertIn('<strike>tarefa teste</strike>', content)

    def test_template_retorna_quantidade_correta_de_tarefas(self):
        for tarefa in range(10):
            self.criar_tarefa(nome='Estudar Django')
            
        resp = self.client.get(reverse('tarefa:index'))
        content = resp.content.decode('UTF-8')
        resp_context_tarefas = resp.context['tarefas']

        self.assertIn('Estudar Django', content)
        self.assertEqual(len(resp_context_tarefas), 10)

    def test_form_com_metodo_POST_esta_presente_na_pagina(self):
        resp = self.client.get(reverse('tarefa:index'))
        content = resp.content.decode('UTF-8')

        self.assertIn('<form method="POST"', content)

    def test_input_eh_do_tipo_submit_para_salvar_tarefa(self):
        resp = self.client.get(reverse('tarefa:index'))
        content = resp.content.decode('UTF-8')

        self.assertIn('<input type="submit"', content)
