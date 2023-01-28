def func(x):
    return x + 1

def test_assertion():
    assert 1
    print("passed in the assertion test")

def test_answer():
    assert func(4) == 5, "not equal"