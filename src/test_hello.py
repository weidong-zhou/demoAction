import sys, pytest

def test_hello(capsys) :
    from hello import hello

    hello=hello()
    hello.say_hello()
    out, err = capsys.readouterr()
    assert out == "Hello World\n"
