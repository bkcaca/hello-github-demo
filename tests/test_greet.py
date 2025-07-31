import pytest
from src.greet import hello
#from greet import hello

def test_hello_normal_name():
    assert hello("Alice") == "Hello, Alice! Welcome to GitHub Collaboration."

def test_hello_empty_string():
    assert hello("") == "Error: Name cannot be empty!"

def test_hello_whitespace():
    assert hello("   ") == "Error: Name cannot be empty!"

def test_hello_special_chars():
    assert hello("John_Doe123") == "Hello, John_Doe123! Welcome to GitHub Collaboration."

def test_hello_long_name():
    long_name = "A" * 1000
    assert hello(long_name) == f"Hello, {long_name}! Welcome to GitHub Collaboration."

def test_hello_main(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: "Test")
    from src.greet import main
    main()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Hello, Test! Welcome to GitHub Collaboration."
