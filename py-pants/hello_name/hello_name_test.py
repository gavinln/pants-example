from hello_name.hello_name import greet


def test_greet():
    assert greet("John") == "Hello John"
