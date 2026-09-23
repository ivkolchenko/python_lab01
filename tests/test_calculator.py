# import pytest
#
# from src.toolkit.calculator import calculator
# from src.toolkit.errors import *
#
# def test_calculator_positive():
#     """Тесты с положительным исходом"""
#     assert calculator('1+3') == 4
#
#     assert calculator('2 - 4') == -2
#
#     assert abs(calculator('0.42 + 0.104') - 0.524) < 0.0001
#
#     assert calculator("-2 + - 2") == -4
#
#     assert abs(calculator('-1.23 + 45.6') - 44.37) < 0.0001
#
#     assert calculator('11*3') == 33
#
#     assert abs(calculator('11/3') - 3.66666) < 0.0001
#
#     assert calculator('2 + 2*2') == 6
#
#     assert abs(calculator('17+3 / 2') - 18.5) < 0.0001
#
#     assert abs(calculator('16/ 4 - 11*2 + 14') + 4) < 0.0001
#
#     assert calculator('123*0') == 0
#
#     assert abs(calculator('0/321 + 1') - 1) < 0.0001
#
# def test_calculator_negative():
#     """Тесты с отрицательным исходом"""
#     with pytest.raises(EmptyExpressionError):
#         calculator('')
#
#     with pytest.raises(EmptyExpressionError):
#         calculator('   ')
#
#     with pytest.raises(WrongSymbolError):
#         calculator('6! + 2')
#
#     with pytest.raises(WrongSymbolError):
#         calculator('(14+2)*3')
#
#     with pytest.raises(OperatorAtFirstPositionError):
#         calculator('*12 + 3')
#
#     with pytest.raises(OperatorAtLastPositionError):
#         calculator('12+1-3-')
#
#     with pytest.raises(OperatorAtLastPositionError):
#         calculator('12 -5 +4 /')
#
#     with pytest.raises(TwoOperatorsError):
#         calculator('14**2')
#
#     with pytest.raises(TwoOperatorsError):
#         calculator('123+ /44')
#
#     with pytest.raises(TwoOperatorsError):
#         calculator('1---4')
#
#     with pytest.raises(DivisionByZeroError):
#         calculator('89 + 3 * 2 + 3/0 - 4')
