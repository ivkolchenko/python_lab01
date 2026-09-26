from toolkit.constants import OPERATORS_PRIORITY, OPERATORS, OPERATORS_WITHOUT_BRACKET
from toolkit.errors import (TwoOperatorsError, TwoOperandsError, BracketError,
                            OperatorAtLastPositionError, OperatorAtFirstPositionError,
                            EmptyExpressionError)


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
    is_negative_token: bool = False
    is_unary_sign: bool = False

    for i, token in enumerate(tokens):

        if token in OPERATORS:
            #Если попадается оператор
            match token:
                case '(':
                    count_brackets += 1
                    new_token_bracket: str = token if not is_negative_token else '-' + token
                    result.append(new_token_bracket)
                    is_negative_token = False
                    is_unary_sign = False

                case ')':
                    if count_brackets < 1:
                        raise BracketError('Пропущена открывающая скобка')
                    elif tokens[i - 1] in OPERATORS and OPERATORS_PRIORITY[tokens[i - 1]] != 0:
                        raise BracketError('Оператор перед закрывающей скобкой')
                    elif tokens[i - 1] == '(':
                        raise BracketError('Пустое выражение в скобках')
                    else:
                        count_brackets -= 1
                        result.append(token)

                case _:
                    if (len(result) != 0 and not is_unary_sign and
                          (result[-1] not in OPERATORS or result[-1] == ')')):
                        #Если на вершине результата нет оператора, он добавляется
                        result.append(token)

                    elif OPERATORS_PRIORITY[token] == 1:
                        #Обработка унарных знаков
                        is_unary_sign = True
                        is_negative_token ^= (token == '-')

                    else:
                        raise TwoOperatorsError('Два бинарных оператора подряд')

        else:
            #Если не оператор - значит операнд
            if len(result) == 0 or result[-1] in OPERATORS:
                #Проверка на унарный знак
                new_token: str = token if not is_negative_token else '-' + token
                result.append(new_token)
                is_negative_token = False
                is_unary_sign = False

            else:
                raise TwoOperandsError('Два операнда подряд')

    if count_brackets != 0:
        raise BracketError('Пропущена закрывающая скобка')

    return result
