import pytest
"""
Write a function that determines if all alpha input_str[idx]acters in a string are surrounded 
(the input_str[idx]acters immediately before and after) by a plus sign.
Function should return false if any alpha input_str[idx]acter present in the string isn't 
surrounded by a plus sign. Otherwise the function should return true.
"""

NORMAL, PLUS, ALPHA, ERROR = 0, 1, 2, 3


# NORMAL, TESTE, PLUS
# NORMAL, TESTE, NORMAL
# NORMAL, TESTE, RAISE
# PLUS, TESTE, PLUS
# PLUS, TESTE, ALPHA
# PLUS, TESTE, NORMAL
# ALPHA, TESTE, PLUS
# ALPHA, TESTE, ALPHA
# ALPHA, TESTE, RAISE

def symbols(s: str) -> bool:
    state = NORMAL

    for char in s:
        if state == NORMAL:
            if char == "+":
                state = PLUS
            elif not char.isalpha():
                continue
            else:
                state = ERROR
        elif state == PLUS:
            if char == "+":
                continue
            elif char.isalpha():
                state = ALPHA
            else:
                state = NORMAL
        elif state == ALPHA:
            if char == "+":
                state = PLUS
            elif char.isalpha():
                continue
            else:
                state = ERROR
        elif state == "ERROR":
            break

    return state not in (ALPHA, ERROR)


def test_main():
    assert symbols("") is True
    assert symbols("0") is True
    assert symbols("123") is True
    assert symbols("01%2-@") is True
    assert symbols("+a+") is True
    assert symbols("+1+") is True
    assert symbols("+ab+") is True
    assert symbols("+ab++") is True
    assert symbols("+Z+Y+") is True
    assert symbols("123+1+ab+a+") is True
    assert symbols("+a+b+7") is True
    assert symbols("+a+=5=+d+") is True
    assert symbols("12+ab+a+12") is True

    assert symbols("a") is False
    assert symbols("a+") is False
    assert symbols("+a") is False
    assert symbols("-a+") is False
    assert symbols("+a-") is False
    assert symbols("-a-") is False
    assert symbols("+ab1+") is False
    assert symbols("+a1b+") is False
    assert symbols("+1ab+") is False
    assert symbols("+ab+a") is False
    assert symbols("+a+b=") is False


if __name__ == "__main__":
    pytest.main(["-s"], __file__)
