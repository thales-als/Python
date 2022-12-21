from codigo.bytebank import Funcionario
import pytest
from pytest import mark


class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        # Given-Contexto
        entrada = '13/03/2000'
        esperado = 22

        # When-Ação
        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade()

        # Then-Desfecho
        assert resultado == esperado

    def test_quando_sobrenome_recebe_Thales_Souza_deve_retornar_Souza(self):
        # Given-Contexto
        entrada = ' Thales Souza '
        esperado = 'Souza'

        # When-Ação
        thales = Funcionario(entrada, '11/11/2000', 1111)
        resultado = thales.sobrenome()

        # Then-Desfecho
        assert resultado == esperado

    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        # Given-Contexto
        entrada_salario = 100000
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        # When-Ação
        funconario_teste = Funcionario(
            entrada_nome, '11/11/2000', entrada_salario)
        funconario_teste.decrescimo_salario()
        resultado = funconario_teste.salario

        # Then-Desfecho
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        # Given-Contexto
        entrada = 1000
        esperado = 100

        # When-Ação
        funconario_teste = Funcionario('teste', '11/11/2000', entrada)
        resultado = funconario_teste.calcular_bonus()

        # Then-Desfecho
        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_100000000_deve_retornar_exception(self):
        with pytest.raises(Exception):
            # Given-Contexto
            entrada = 100000000

            # When-Ação
            funconario_teste = Funcionario('teste', '11/11/2000', entrada)
            resultado = funconario_teste.calcular_bonus()

            # Then-Desfecho
            assert resultado
