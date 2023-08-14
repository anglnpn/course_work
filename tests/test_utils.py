"""
Импорт класса и функции.
"""
from classes import Operation
from utils import unpacking_json
import pytest


def test_unpacking():
    """
    Тест функции.
    Проверка распаковки файла.
    """
    a = unpacking_json("tests/operations.json")
    assert len(a) == 5


def test_get_from_and_to():
    """
    Тест класса
    """
    operation = Operation("20190826", "31957.58", "руб.", "Перевод организации",
                          "Счет 64686473678894779589", "Maestro 1596837868705199")
    assert str(
        operation) == '26.08.2019 Перевод организации\n''Maestro 1596 83** **** 5199 -> Счет **9589\n''31957.58 руб.\n'
