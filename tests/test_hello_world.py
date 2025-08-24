import sys

from hello_world import echo


def test_echo(monkeypatch, capsys):
    monkeypatch.setattr(sys, 'argv', [sys.argv[0], "my_name"])
    echo.main()
    output = capsys.readouterr()
    assert output.out == "Hello world: my_name\n"
