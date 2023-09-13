from helloAgain import hello

def test_default():
    assert hello() == 'Hello, World'
def test_arguments():
    assert hello('Roy') == 'Hello, Roy'
