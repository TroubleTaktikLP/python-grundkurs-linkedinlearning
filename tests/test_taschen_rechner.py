import pytest

from genai_beispiele.taschen_rechner import Taschenrechner

def test_addition():
    tr = Taschenrechner()
    assert tr.sum(1, 2) == 3

def test_subtraktion():
    tr = Taschenrechner()
    assert tr.sub(3, 2) == 1

def test_multiplikation():
    tr = Taschenrechner()
    assert tr.mul(2, 2) == 4

def test_division():
    tr = Taschenrechner()
    assert tr.div(4, 2) == 2
    with pytest.raises(ValueError):
        tr.div(4, 0)