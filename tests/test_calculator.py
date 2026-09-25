import pytest

from toolkit.calculation import calculator
from decimal import Decimal
from toolkit.errors import (EmptyExpressionError, WrongSymbolError,
                     OperatorAtFirstPositionError, OperatorAtLastPositionError,
                     BracketError, TwoOperatorsError, DivisionByZeroError,
                     TwoOperandsError)


def test_calculator_positive() -> None:
    """Тесты с положительным исходом"""
    assert calculator('1+3') == 4

    assert calculator('2 - 4') == -2

    assert calculator('0.42 + 0.104') == Decimal('0.524')

    assert calculator("-2 + - 2") == -4

    assert calculator('-1.23 + 45.6') == Decimal('44.37')

    assert calculator('11*3') == 33

    assert calculator('2 + 2*2') == 6

    assert calculator('17+3 / 2') == Decimal('18.5')

    assert calculator('16/ 4 - 11*2 + 14') == -4

    assert calculator('123*0') == 0

    assert calculator('0/321 + 1') == 1

    assert calculator('+2-2') == 0

    assert calculator('-(2-3)*7') == 7

    assert calculator('14 + -(3 + -(4+2))') == 17

    assert calculator('33 // (12%5)') == 16

    assert calculator('-13%8') == 3


def test_calculator_negative() -> None:
    """Тесты с отрицательным исходом"""
    with pytest.raises(EmptyExpressionError):
        calculator('')

    with pytest.raises(EmptyExpressionError):
        calculator('   ')

    with pytest.raises(WrongSymbolError):
        calculator('6! + 2')

    with pytest.raises(OperatorAtFirstPositionError):
        calculator('*12 + 3')

    with pytest.raises(OperatorAtLastPositionError):
        calculator('12+1-3-')

    with pytest.raises(OperatorAtLastPositionError):
        calculator('12 -5 +4 /')

    with pytest.raises(TwoOperatorsError):
        calculator('14**2')

    with pytest.raises(TwoOperatorsError):
        calculator('123+ /44')

    with pytest.raises(TwoOperatorsError):
        calculator('1*/4')

    with pytest.raises(DivisionByZeroError):
        calculator('89 + 3 * 2 + 3/0 - 4')

    with pytest.raises(BracketError):
        calculator('133 + ( 14 - 2')

    with pytest.raises(BracketError):
        calculator('5 - ( 77 * 2 + ( 15 - 3)')

    with pytest.raises(BracketError):
        calculator('1+ ()')

    with pytest.raises(BracketError):
        calculator('15 - (4+6*)')

    with pytest.raises(TwoOperandsError):
        calculator('1 5 - 2')
