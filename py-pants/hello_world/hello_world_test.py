from hello_world.hello_world import greet, print_greet


def test_greet():
    assert greet() == "Hello world"


def test_print_greet():
    print_greet()
    assert False
