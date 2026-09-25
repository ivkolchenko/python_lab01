import pytest

from toolkit.convertor import convertor
from toolkit.errors import (DifferentQuantitiesError, UnknownQuantityError,
                            NonNumericalValueError, InvalidValueError)


def float_comparison(first_value: float, second_value: float) -> bool:
    """Сравнение числовых значений float с точностью 9 знаков после запятой"""
    return abs(first_value - second_value) <= 1e-9


def test_convertor_positive() -> None:
    """Тесты с положительным исходом"""
    assert float_comparison(convertor('12', 'mm', 'cm'), 1.2)

    assert float_comparison(convertor('12345', 'mm', 'm'), 12.345)

    assert float_comparison(convertor('567890', 'mm', 'km'), 0.56789)

    assert float_comparison(convertor('13.2', 'cm', 'mm'), 132)

    assert float_comparison(convertor('111', 'cm', 'm'), 1.11)

    assert float_comparison(convertor('13579', 'cm', 'km'), 0.13579)

    assert float_comparison(convertor('1', 'm', 'mm'), 1000)

    assert float_comparison(convertor('12', 'm', 'cm'), 1200)

    assert float_comparison(convertor('14', 'm', 'km'), 0.014)

    assert float_comparison(convertor('1.23', 'km', 'mm'), 1230000)

    assert float_comparison(convertor('0.543', 'km', 'cm'), 54300)

    assert float_comparison(convertor('1', 'km', 'm'), 1000)

    assert float_comparison(convertor('112', 'g', 'kg'), 0.112)

    assert float_comparison(convertor('32.22', 'kg', 'g'), 32220)

    assert float_comparison(convertor('15.85', 'k', 'c'), -257.3)

    assert float_comparison(convertor('323', 'k', 'f'), 121.73)

    assert float_comparison(convertor('97', 'c', 'k'), 370.15)

    assert float_comparison(convertor('0', 'c', 'f'), 32)

    assert float_comparison(convertor('121.73', 'f', 'k'), 323)

    assert float_comparison(convertor('32', 'f', 'c'), 0)


def test_convertor_negative() -> None:
    """Тесты с отрицательным исходом"""
    with pytest.raises(DifferentQuantitiesError):
        convertor('23', 'c', 'cm')

    with pytest.raises(DifferentQuantitiesError):
        convertor('55', 'g', 'f')

    with pytest.raises(UnknownQuantityError):
        convertor('3', 'c', 'y')

    with pytest.raises(UnknownQuantityError):
        convertor('231', 't', 'cm')

    with pytest.raises(NonNumericalValueError):
        convertor('twenty one', 'k', 'f')

    with pytest.raises(InvalidValueError):
        convertor('-5', 'm', 'cm')

    with pytest.raises(InvalidValueError):
        convertor('-299', 'c', 'k')
