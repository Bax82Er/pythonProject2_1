import pytest
from src.decorators import log
from unittest.mock import patch


def test_log_success(capsys):
    @log()
    def add(a, b):
        return a + b

    add(1, 2)
    captured = capsys.readouterr()
    assert captured.out == "add ok. Result: 3. Duration: 0.00 ms.\n"


def test_log_error(capsys):
    @log()
    def divide(a, b):
        return a / b

    with pytest.raises(ZeroDivisionError):
        divide(1, 0)

    captured = capsys.readouterr()
    assert "divide error: ZeroDivisionError. Message: division by zero." in captured.err


def test_log_to_file(tmp_path):
    filename = tmp_path / "logfile.txt"

    @log(str(filename))
    def multiply(a, b):
        return a * b

    multiply(2, 3)
    with open(filename, 'r') as file:
        content = file.read()
        assert "multiply ok. Result: 6." in content