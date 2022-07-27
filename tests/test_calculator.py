"""Write simple test cases using pytest and run"""

import pytest

def add(s):
    if s == '':
        return 0
    temp = int(s)
    return temp

def test_if_add_Zero_numbers():
    assert add('') == 0

def test_add_one_number():
    assert add('42') == 42

def test_add_not_a_number():
    with pytest.raises(ValueError):
        add('abcde')
