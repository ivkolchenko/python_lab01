from .constants import OPERATORS_PRIORITY, OPERATORS_WITHOUT_BRACKET
from .errors import DivisionByZeroError, TwoOperandsError
from .tokenization import expression_tokenization
from .validation import expression_validation
from decimal import Decimal, getcontext, ROUND_HALF_DOWN


def shunting_yard_algorithm(tokens: list[str]) -> list[Decimal | str]:
    """Преобразование выражения в постфиксную форму
    для корректного вычесления"""
    stack: list[str] = []  #стек оперторов
    result: list[Decimal | str] = []  #итоговый выход

    for token in tokens:

        if token == '(':
            stack.append(token)
        elif token == '-(':
            stack.append(token)
        elif token == ')':
            while stack[-1] != '-(' and stack[-1] != '(':
                result.append(stack[-1])
                stack.pop(-1)
            if stack[-1] == '-(':
                result.append('n')
            stack.pop(-1)
        elif token in OPERATORS_WITHOUT_BRACKET:
            while (len(stack) > 0 and
                   OPERATORS_PRIORITY[stack[-1]] >= OPERATORS_PRIORITY[token]):
                result.append(stack[-1])
                stack.pop(-1)
            stack.append(token)
        else:
            result.append(Decimal(token))

    for token in reversed(stack):
        result.append(token)

    return result


def expression_calculation(tokens: list[Decimal | str]) -> Decimal:
    """Итоговое вычесление выражения"""
    stack: list[Decimal] = []

    for token in tokens:

        if isinstance(token, Decimal):
            stack.append(token)

        elif token == 'n':
            stack[-1] *= -1

        elif token == '*':
            stack[-2] *= stack[-1]
            stack.pop(-1)

        elif token == '/':
            if stack[-1] == 0:
                raise DivisionByZeroError('Деление на ноль')
            else:
                stack[-2] /= stack[-1]
                stack.pop(-1)

        elif token == '//':
            if stack[-1] == 0:
                raise DivisionByZeroError('Деление на ноль')
            else:
                stack[-2] //= stack[-1]
                stack.pop(-1)

        elif token == '%':
            if stack[-1] == 0:
                raise DivisionByZeroError('Взятие остатка от деления на ноль')
            else:
                stack[-2] = ((stack[-2] % stack[-1]) + stack[-1]) % stack[-1]
                stack.pop(-1)

        elif token == '-':
            stack[-2] -= stack[-1]
            stack.pop(-1)

        elif token == '+':
            stack[-2] += stack[-1]
            stack.pop(-1)

    if len(stack) == 1:
        return stack[0]
    else:
        raise TwoOperandsError('Пропущен оператор')


def calculator(expression: str) -> Decimal:
    """Тело калькулятора"""
    getcontext().rounding = ROUND_HALF_DOWN

    expression_tokens: list[str] = expression_tokenization(expression)
    expression_tokens = expression_validation(expression_tokens)

    expression_in_postfix_form: list[str | Decimal] = shunting_yard_algorithm(expression_tokens)

    return expression_calculation(expression_in_postfix_form)
