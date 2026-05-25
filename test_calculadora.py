from calculadora import add, subtract, multiply

def test_add():
    assert add(2, 3) == 5

def test_subtract():
    assert subtract(5, 2) == 3

def test_multiply():
    assert multiply(3, 4) == 12
    
def test_divide():
    from calculadora import divide
    assert divide(10, 2) == 5
    try:
        divide(10, 0)
        assert False, "Expected ValueError for division by zero"
    except ValueError:
        pass