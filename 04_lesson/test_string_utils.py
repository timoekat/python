import pytest
from string_utils import StringUtils


string_utils = StringUtils()


@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    ("skypro", "Skypro"),
    ("hello world", "Hello world"),
    ("python", "Python"),
])
def test_capitalize_positive(input_str, expected):
    assert string_utils.capitalize(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [
    ("123abc", "123abc"),
    ("", ""),
    ("   ", "   "),
])
def test_capitalize_negative(input_str, expected):
    assert string_utils.capitalize(input_str) == expected

@pytest.mark.positive
@pytest.mark.parametrize("input_str, expected", [
    (" skypro", "skypro"),
    ("hello world", "hello world"),
    ("    python", "python"),
])

def test_trim_positive(input_str, expected):
     assert string_utils.trim(input_str) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, expected", [         
    ("\t skypro", "\t skypro"),
    ("\n skypro", "\n skypro"),
    ("skypro   ", "skypro   ")
])

def test_trim_negative(input_str, expected):
    assert string_utils.trim(input_str) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "S", True),
    ("SkyPro", "U", False),
    ("Python", "P", True)
])

def test_contains_positive(input_str, symbol, expected):
     assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("Python", " ", False)
    
])

def test_contains_negative(input_str, symbol, expected):
     assert string_utils.contains(input_str, symbol) == expected


@pytest.mark.positive
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "k", "SyPro"),
    ("SkyPro", "Pro", "Sky"),
    ("Python", "P", "ython")
])

def test_delete_symbol_positive(input_str, symbol, expected):
     assert string_utils.delete_symbol(input_str, symbol) == expected


@pytest.mark.negative
@pytest.mark.parametrize("input_str, symbol, expected", [
    ("SkyPro", "", "SkyPro"),
    ("SkyPro", "i", "SkyPro")
])

def test_delete_symbol_negative(input_str, symbol, expected):
     assert string_utils.delete_symbol(input_str, symbol) == expected


