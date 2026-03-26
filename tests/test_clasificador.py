# tests/test_clasificador.py

import pytest
from src.clasificador import clasificar_nota


# -------------------------
# TESTS NORMALES (N)
# -------------------------

def test_suspenso_normal():
    # Arrange
    nota = 3
    # Act
    resultado = clasificar_nota(nota)
    # Assert
    assert resultado == "Suspenso"


def test_aprobado_normal():
    nota = 6
    resultado = clasificar_nota(nota)
    assert resultado == "Aprobado"


# -------------------------
# TESTS DE LÍMITE (L)
# -------------------------

def test_nota_exactamente_cinco():
    nota = 5.0
    resultado = clasificar_nota(nota)
    assert resultado == "Aprobado"


def test_nota_exactamente_siete():
    nota = 7.0
    resultado = clasificar_nota(nota)
    assert resultado == "Notable"


def test_nota_diez():
    nota = 10
    resultado = clasificar_nota(nota)
    assert resultado == "Sobresaliente"


def test_nota_499():
    nota = 4.99
    resultado = clasificar_nota(nota)
    assert resultado == "Suspenso"


def test_nota_999():
    nota = 9.99
    resultado = clasificar_nota(nota)
    assert resultado == "Sobresaliente"


# -------------------------
# TESTS DE ERROR (E)
# -------------------------

def test_nota_negativa():
    with pytest.raises(ValueError):
        clasificar_nota(-1)


def test_nota_mayor_diez():
    with pytest.raises(ValueError):
        clasificar_nota(11)


def test_tipo_incorrecto():
    with pytest.raises(TypeError):
        clasificar_nota("ocho")
