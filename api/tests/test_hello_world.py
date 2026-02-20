from models import HelloWorld

def test_HelloWorld():
    hello_world = HelloWorld("coucou")
    assert hello_world.id is not None