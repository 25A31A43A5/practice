from app import calculator

def test_add():
    assert calculator.add(2,3)==5

def test_subtract():
    assert calculator.subtract(30,10)==20

def test_multiply():
    assert calculator.multiply(1,2)==2

def test_divide():
    assert calculator.divide(10,2)==5.0

def test_result():
    assert calculator.result("+",1,2)==3