import sys, pytest
from hello import hello

def test_hello(capsys) :
    hello=hello()
    hello.say_hello()
    out, err = capsys.readouterr()
    assert out == "Hello World\n"
