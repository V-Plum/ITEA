from homework_7.misc_inputs import misc_inputs
from io import StringIO


def test_confirm(monkeypatch):
    yes_inputs = StringIO('y\n')
    monkeypatch.setattr('sys.stdin', yes_inputs)
    assert misc_inputs.confirm("Sure") is True


def test_confirm_2(monkeypatch):
    yes_inputs = StringIO('n\n')
    monkeypatch.setattr('sys.stdin', yes_inputs)
    assert misc_inputs.confirm("Sure") is False


def test_create_list(monkeypatch):
    list_inputs = StringIO('2\nBlah\nBlah2\n')
    monkeypatch.setattr('sys.stdin', list_inputs)
    assert misc_inputs.create_list() == ["Blah", "Blah2"]


def test_create_list_2(monkeypatch):
    list_inputs = StringIO('item_1\nitem_2\nitem_3\n')
    monkeypatch.setattr('sys.stdin', list_inputs)
    assert misc_inputs.create_list(3) == ["item_1", "item_2", "item_3"]


def test_create_list_3(monkeypatch):
    list_inputs = StringIO('\ny\n')
    monkeypatch.setattr('sys.stdin', list_inputs)
    assert misc_inputs.create_list(3) == []
