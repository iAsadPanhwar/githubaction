from src.maths_operations import add, sub

def test_add():
    assert add(2,3)==5
    assert add(4,7)==11
    assert add(10,5)==15
    
def test_sub():
    assert sub(6,3)==3
    assert sub(1,-1)==2
    assert sub(100,50)==50