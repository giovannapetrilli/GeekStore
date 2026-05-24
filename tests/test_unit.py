from main import calcular_desconto
from main import processar_pedido
from unittest.mock import Mock
import pytest

def test_desconto_geek20():

    resultado = calcular_desconto(100, "GEEK20")

    assert resultado == 80


def test_sem_desconto():

    resultado = calcular_desconto(100, "")

    assert resultado == 100


def test_pagamento_aprovado():

    gateway = Mock()

    gateway.cobrar.return_value = True

    resultado = processar_pedido(
        100,
        "1234",
        gateway
    )

    assert resultado == "Compra aprovada!"


def test_pagamento_recusado():

    gateway = Mock()

    gateway.cobrar.return_value = False

    with pytest.raises(ValueError):
        processar_pedido(100, "1234", gateway)


def test_valor_invalido():

    gateway = Mock()

    with pytest.raises(ValueError):
        processar_pedido(0, "1234", gateway)