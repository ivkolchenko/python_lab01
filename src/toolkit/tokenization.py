from .constants import TOKEN_PATTERN
from .errors import WrongSymbolError


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
