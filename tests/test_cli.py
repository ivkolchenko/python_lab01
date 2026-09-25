from typer.testing import CliRunner
from toolkit.__main__ import app

runner = CliRunner()

def test_calc_positive() -> None:
    result = runner.invoke(app, ['calc', '+1 - 2 * (3 - -4)'])

    assert result.exit_code == 0
    assert result.stdout.strip() == '-13'


def test_calc_negative() -> None:
    result = runner.invoke(app, ['calc', '1--3+'])

    assert result.exit_code == 2
    assert result.stderr.strip() == 'Ошибка: Оператор в конце выражения'


def test_convert_positive() -> None:
    result = runner.invoke(app, ['convert', '67.67', '--from', 'kg', '--to', 'g'])

    assert result.exit_code == 0
    assert result.stdout.strip() == '67670.0'


def test_convert_negative() -> None:
    result = runner.invoke(app, ['convert', '67.67', '--from', 'g', '--to', 'k'])

    assert result.exit_code == 2
    assert result.stderr.strip() == 'Ошибка: Нельзя перевести в эту величину'
