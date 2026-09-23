from .constants import (OPERATORS, OPERATORS_PRIORITY, TOKEN_PATTERN,
                        OPERATORS_WITHOUT_BRACKET, OPENING_BRACKET_VARIATIONS)
from .errors import (EmptyExpressionError, WrongSymbolError,
                     OperatorAtFirstPositionError, OperatorAtLastPositionError,
                     BracketError, TwoOperatorsError, DivisionByZeroError)
from decimal import Decimal

def expression_tokenization(expression: str) -> list[str]:
    """Разбиение выражения на токены"""

    result: list[str] = []
    position: int = 0

    while position < len(expression):
        if expression[position] == ' ':
            position += 1
            continue

        token = TOKEN_PATTERN.match(expression, position)

        if token is None:
            raise WrongSymbolError(f'Недопустимый символ: {expression[position]}')

        result.append(token.group())
        position = token.end()

    return result


def expression_validation(tokens: list[str]) -> list[str]:
    """Проверка выражения на корректность
    и склеивание унарных знаков"""

    if len(tokens) == 0:
        raise EmptyExpressionError('Пустое выражение')

    if tokens[0] in OPERATORS_WITHOUT_BRACKET and OPERATORS_PRIORITY[tokens[0]] > 1:
        raise OperatorAtFirstPositionError('Оператор в начале выражения')

    if tokens[-1] in OPERATORS_WITHOUT_BRACKET:
        raise OperatorAtLastPositionError('Оператор в конце выражения')

    result: list[str] = []
    count_brackets: int = 0
    for i, token in enumerate(tokens):
        if token in OPERATORS:
            if token in OPENING_BRACKET_VARIATIONS:
                result.append(token)
                count_brackets += 1
            elif token == ')':
                if count_brackets < 1:
                    raise BracketError('Пропущена открывающая скобка')
                else:
                    count_brackets -= 1
                    result.append(token)
            elif (len(result) != 0 and
                  (result[-1] not in OPERATORS or result[-1] == ')')):
                result.append(token)
            elif (OPERATORS_PRIORITY[token] == 1 and
                  (tokens[i + 1] not in OPERATORS or tokens[i + 1] == '(')):
                tokens[i + 1] = token + tokens[i + 1]
            else:
                raise TwoOperatorsError('Два оператора подряд')
        else:
            result.append(token)

    if count_brackets != 0:
        raise BracketError('Пропущена закрывающая скобка')

    return result


def shunting_yard_algorithm(tokens: list[str]) -> list[Decimal | str]:
    """Преобразование выражения в постфиксную форму
    для корректного вычесления"""
    stack: list[str] = []  #стек оперторов
    result: list[Decimal | str] = []  #итоговый выход

    negative_bracket_count: int = 0
    for token in tokens:
        if token == '(' or token == '+(':
            stack.append('(')
        elif token == '-(':
            stack.append('(')
            negative_bracket_count += 1
        elif token == ')':
            while stack[-1] != '(':
                result.append(stack[-1])
                stack.pop(-1)
            stack.pop(-1)
            if negative_bracket_count > 0:
                negative_bracket_count -= 1
        elif token in OPERATORS_WITHOUT_BRACKET:
            while (len(stack) > 0 and
                   OPERATORS_PRIORITY[stack[-1]] >= OPERATORS_PRIORITY[token]):
                result.append(stack[-1])
                stack.pop(-1)
            stack.append(token)
        else:
            if negative_bracket_count%2 == 0:
                result.append(Decimal(token))
            else:
                result.append(-Decimal(token))

    for token in reversed(stack):
        result.append(token)

    return result


def expression_calculation(tokens: list[Decimal | str]) -> Decimal:
    """Итоговое вычесление выражения"""
    stack: list[Decimal] = []

    for token in tokens:

        if isinstance(token, Decimal):
            stack.append(token)

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
                stack[-2] %= stack[-1]
                stack.pop(-1)

        elif token == '-':
            stack[-2] -= stack[-1]
            stack.pop(-1)

        elif token == '+':
            stack[-2] += stack[-1]
            stack.pop(-1)

    return stack[0]


def calculator(expression: str) -> Decimal:
    """Тело калькулятора"""
    expression_tokens: list[str] = expression_tokenization(expression)
    expression_tokens = expression_validation(expression_tokens)

    expression_in_postfix_form: list[str | Decimal] = shunting_yard_algorithm(expression_tokens)

    return expression_calculation(expression_in_postfix_form)
