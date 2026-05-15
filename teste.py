import pytest
from operacoes.adicao import somar
from operacoes.subtracao import subtrair
from operacoes.multiplicacao import multiplicar
from operacoes.divisao import dividir

def test_somar():
    assert somar(2, 3) == 5

def test_subtrair():
    assert subtrair(5, 3) == 2

def test_multiplicar():
    assert multiplicar(4, 3) == 12

def test_dividir():
    assert dividir(10, 2) == 5

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(5, 0)