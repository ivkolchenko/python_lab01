from .constants import (WEIGHT_UNITS, WEIGHT_COEFFICIENTS, LENGTH_UNITS,
                        LENGTH_COEFFICIENTS, TEMPERATURE_UNITS)
from .errors import DifferentQuantitiesError, UnknownQuantityError


def weight_convertor(value: float, from_unit: str, to_unit: str) -> float:
    """Перевод величин массы по формуле:
    value *  COEFFICIENTS[from_unit] / COEFFICIENTS[to_unit]"""
    if to_unit in WEIGHT_UNITS:
        return value * WEIGHT_COEFFICIENTS[from_unit] / WEIGHT_COEFFICIENTS[to_unit]
    elif to_unit in LENGTH_UNITS or to_unit in TEMPERATURE_UNITS:
        raise DifferentQuantitiesError('Нельзя перевести в эту величину')
    else:
        raise UnknownQuantityError('Неизвестная величина: ' + str(to_unit))


def length_convertor(value: float, from_unit: str, to_unit: str) -> float:
    """Перевод величин длины по формуле:
    value *  COEFFICIENTS[from_unit] / COEFFICIENTS[to_unit]"""
    if to_unit in LENGTH_COEFFICIENTS:
        return value * LENGTH_COEFFICIENTS[from_unit] / LENGTH_COEFFICIENTS[to_unit]
    elif to_unit in WEIGHT_UNITS or to_unit in TEMPERATURE_UNITS:
        raise DifferentQuantitiesError('Нельзя перевести в эту величину')
    else:
        raise UnknownQuantityError('Неизвестная величина: ' + str(to_unit))

def temperature_convertor(value: float, from_unit: str, to_unit: str) -> float:
    """Перевод величин температуры в кельвины,
    затем в необходмую величину"""
    if to_unit in TEMPERATURE_UNITS:
        temperature = value
        # Перевод в кельвины
        if from_unit == 'c':
            temperature += 273.15
        elif from_unit == 'f':
            temperature += 459.67
            temperature *= 5 / 9
        # Перевод в необходимую величину
        if to_unit == 'c':
            temperature -= 273.15
        elif to_unit == 'f':
            temperature *= 9 / 5
            temperature -= 459.67
        return temperature

    elif to_unit in WEIGHT_UNITS or to_unit in LENGTH_UNITS:
        raise DifferentQuantitiesError('Нельзя перевести в эту величину')
    else:
        raise UnknownQuantityError('Неизвестная величина: ' + str(to_unit))

def convertor(value: float, from_unit: str, to_unit: str) -> float:
    """Тело конвертора"""
    from_unit = from_unit.lower()
    to_unit = to_unit.lower()

    if from_unit in WEIGHT_UNITS:
        return weight_convertor(value, from_unit, to_unit)
    elif from_unit in LENGTH_UNITS:
        return length_convertor(value, from_unit, to_unit)
    elif from_unit in TEMPERATURE_UNITS:
        return temperature_convertor(value, from_unit, to_unit)
    else:
        raise UnknownQuantityError('Неизвестная величина: ' + str(from_unit))
