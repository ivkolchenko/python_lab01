import re

OPERATORS: list = ['+', '-', '*', '/', '(', ')', '//', '%', '-(', '+(']
OPENING_BRACKET_VARIATIONS: list[str] = ['(', '-(', '+(']
TOKEN_PATTERN: re.Pattern = re.compile(r"//|[+\-*/%()]|\d+(?:\.\d+)?")
OPERATORS_WITHOUT_BRACKET: list = ['+', '-', '*', '/', '//', '%']
OPERATORS_PRIORITY: dict = {'+': 1, '-': 1, '*': 2, '/': 2, '//': 2, '%': 2, '(': 0, ')': 0}
LENGTH_UNITS: list = ['mm', 'cm', 'm', 'km']
LENGTH_COEFFICIENTS: dict = {'mm': 1, 'cm': 10, 'm': 1000, 'km': 1000000}
WEIGHT_UNITS: list = ['g', 'kg']
WEIGHT_COEFFICIENTS: dict = {'g': 1, 'kg': 1000}
TEMPERATURE_UNITS: list = ['c', 'f', 'k']
