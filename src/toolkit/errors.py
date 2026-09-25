class ToolkitError(Exception):
    """Базовая ошибка"""

class EmptyExpressionError(ToolkitError):
    """Ошибка пустого выражения"""
    pass

class WrongSymbolError(ToolkitError):
    """Ошибка недопустимого символа в выражении"""
    pass

class OperatorAtFirstPositionError(ToolkitError):
    """Ошибка оператора в начале выражения"""
    pass

class TwoOperandsError(ToolkitError):
    """Ошибка двух операндов подряд"""
    pass

class OperatorAtLastPositionError(ToolkitError):
    """Ошибка оператора в конце выражения"""
    pass

class TwoOperatorsError(ToolkitError):
    """Ошибка двух операторов подряд в выражении"""
    pass

class BracketError(ToolkitError):
    """Ошибка со скобками"""
    pass

class DivisionByZeroError(ToolkitError):
    """Ошибка деления на ноль в выражении"""
    pass

class DifferentQuantitiesError(ToolkitError):
    """Ошибка несовместнимых величин перевода"""
    pass

class UnknownQuantityError(ToolkitError):
    """Ошибка неизвестных величин перевода"""
    pass

class NonNumericalValueError(ToolkitError):
    """Ошибка нечислового значения"""
    pass

class InvalidValueError(ToolkitError):
    """Ошибка недопустимого значения для какой-либо системы величин"""
    pass
