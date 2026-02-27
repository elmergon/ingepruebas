from calculadora import Calculadora

def test_add():
    calc = Calculadora()
    assert calc.add(2, 3) == 5

def test_subtract():
    calc = Calculadora()
    assert calc.subtract(10, 5) == 5