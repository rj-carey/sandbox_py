import pytest
from structures.data_store import DataStore

def test_add():
    result = DataStore.add("item")
    assert result == "add() not implemented for this structure type."

def test_insert():
    result = DataStore.insert(0, "item")
    assert result == "insert() not implemented for this structure type."

def test_get():
    result = DataStore.get(0)
    assert result == "get() not implemented for this structure type."

def test_remove():
    result = DataStore.remove("item")
    assert result == "remove() not implemented for this structure type."

def test_set():
    result = DataStore.set(0, "item")
    assert result == "set() not implemented for this structure type."

def test_peek():
    result = DataStore.peek(0)
    assert result == "peek() not implemented for this structure type."
