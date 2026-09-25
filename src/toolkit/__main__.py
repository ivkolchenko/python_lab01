from typing import Annotated
from .calculation import calculator
from .convertor import convertor
from .errors import ToolkitError

import typer

app = typer.Typer()

@app.command(context_settings={'ignore_unknown_options': True})
def calc(expression: str) -> None:
    """Консольная команда калькулятора"""
    try:
        result = calculator(expression)
        typer.echo(result)
    except ToolkitError as error:
        typer.echo(f'Ошибка: {error}', err = True)
        raise typer.Exit(code = 2)

@app.command(context_settings={'ignore_unknown_options': True})
def convert(
        value: str,
        from_unit: Annotated[str, typer.Option('--from')],
        to_unit: Annotated[str, typer.Option('--to')]) -> None:
    """Консольная команда конветора"""
    try:
        result = convertor(value, from_unit, to_unit)
        typer.echo(result)
    except ToolkitError as error:
        typer.echo(f'Ошибка: {error}', err = True)
        raise typer.Exit(code = 2)


if __name__ == '__main__':
    app()
