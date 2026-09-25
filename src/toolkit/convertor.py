from .constants import (WEIGHT_UNITS, WEIGHT_COEFFICIENTS, LENGTH_UNITS,
                        LENGTH_COEFFICIENTS, TEMPERATURE_UNITS)
from .errors import DifferentQuantitiesError, UnknownQuantityError, NonNumericalValueError, InvalidValueError
from decimal import Decimal, getcontext, ROUND_HALF_DOWN, InvalidOperation


def weight_convertor(value: Decimal, from_unit: str, to_unit: str) -> Decimal:
    """Перевод величин массы по формуле:
    value *  COEFFICIENTS[from_unit] / COEFFICIENTS[to_unit]"""
    if value < 0:
        raise InvalidValueError('Масса не может быть меньше нуля')

    if to_unit in WEIGHT_UNITS:
        return value * WEIGHT_COEFFICIENTS[from_unit] / WEIGHT_COEFFICIENTS[to_unit]
    elif to_unit in LENGTH_UNITS or to_unit in TEMPERATURE_UNITS:
        raise DifferentQuantitiesError('Нельзя перевести в эту величину')
    else:
        raise UnknownQuantityError('Неизвестная величина: ' + str(to_unit))


def length_convertor(value: Decimal, from_unit: str, to_unit: str) -> Decimal:
    """Перевод величин длины по формуле:
    value *  COEFFICIENTS[from_unit] / COEFFICIENTS[to_unit]"""
    if value < 0:
        raise InvalidValueError('Длина не может быть меньше нуля')

    if to_unit in LENGTH_COEFFICIENTS:
        return value * LENGTH_COEFFICIENTS[from_unit] / LENGTH_COEFFICIENTS[to_unit]
    elif to_unit in WEIGHT_UNITS or to_unit in TEMPERATURE_UNITS:
        raise DifferentQuantitiesError('Нельзя перевести в эту величину')
    else:
        raise UnknownQuantityError('Неизвестная величина: ' + str(to_unit))

def temperature_convertor(value: Decimal, from_unit: str, to_unit: str) -> Decimal:
    """Перевод величин температуры в кельвины,
    затем в необходмую величину"""
    if to_unit in TEMPERATURE_UNITS:
        temperature:Decimal = value
        # Перевод в кельвины
        if from_unit == 'c':
            temperature += Decimal('273.15')
        elif from_unit == 'f':
            temperature += Decimal('459.67')
            temperature *= 5
            temperature /= 9

        if temperature < 0:
            raise InvalidValueError('Температура не может быть меньше абсолютного нуля')

        # Перевод в необходимую величину
        if to_unit == 'c':
            temperature -= Decimal('273.15')
        elif to_unit == 'f':
            temperature *= 9
            temperature /= 5
            temperature -= Decimal('459.67')
        return temperature

    elif to_unit in WEIGHT_UNITS or to_unit in LENGTH_UNITS:
        raise DifferentQuantitiesError('Нельзя перевести в эту величину')
    else:
        raise UnknownQuantityError('Неизвестная величина: ' + str(to_unit))

def convertor(value: str, from_unit: str, to_unit: str) -> float:
    """Тело конвертора"""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()
    getcontext().rounding = ROUND_HALF_DOWN
    try:
        decimal_value = Decimal(value)
    except InvalidOperation:
        raise NonNumericalValueError('Нечисловое значение аргумента VALUE')

    if from_unit in WEIGHT_UNITS:
        return float(weight_convertor(decimal_value, from_unit, to_unit))
    elif from_unit in LENGTH_UNITS:
        return float(length_convertor(decimal_value, from_unit, to_unit))
    elif from_unit in TEMPERATURE_UNITS:
        return float(temperature_convertor(decimal_value, from_unit, to_unit))
    else:
        raise UnknownQuantityError('Неизвестная величина: ' + str(from_unit))
