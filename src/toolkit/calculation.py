from .constants import OPERATORS_PRIORITY, OPERATOR_DICT
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

        match token:
            case '(' | '-(':
                stack.append(token)

            case ')':
                while stack[-1] != '-(' and stack[-1] != '(':
                    result.append(stack[-1])
                    stack.pop()
                if stack[-1] == '-(':
                    result.append('n')
                stack.pop()

            case '+'| '-' | '*' | '/' | '//' | '%':
                while (len(stack) > 0 and
                       OPERATORS_PRIORITY[stack[-1]] >= OPERATORS_PRIORITY[token]):
                    result.append(stack[-1])
                    stack.pop()
                stack.append(token)

            case _:
                result.append(Decimal(token))

    for token in reversed(stack):
        result.append(token)

    return result


def expression_calculation(tokens: list[Decimal | str]) -> Decimal:
    """Итоговое вычесление выражения"""
    stack: list[Decimal] = []

    for token in tokens:

        if token in OPERATOR_DICT.keys():
            #Все операторы, кроме унарного '-' и '%'
            try:
                stack[-2] = OPERATOR_DICT[token](stack[-2], stack[-1])
                stack.pop()
            except ZeroDivisionError:
                raise DivisionByZeroError

        elif token == 'n':
            stack[-1] *= -1

        elif token == '%':
            stack[-2] = (stack[-2] % stack[-1] + stack[-1]) % stack[-1]
            stack.pop()

        elif isinstance(token, Decimal):
            stack.append(token)


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
