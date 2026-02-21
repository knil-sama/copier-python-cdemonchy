from models.hello_world import HelloWorld

def test_HelloWorld():
    hello_world = HelloWorld(value="coucou")
    assert isinstance(hello_world, HelloWorld)
    assert "coucou"==hello_world.value