from helloAgain import hello

def test_argument():
    for name in ['Hermione', 'Harry', 'Ron']:
        assert hello(name) == f'Hello, {name}'
    
def test_default():
    assert hello() == 'Hello, World'
    