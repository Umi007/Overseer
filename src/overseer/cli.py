"""Command-line entry point."""

from typing import Annotated

import typer

app = typer.Typer(no_args_is_help=True)


@app.callback()
def main() -> None:
    """Research whether an Amazon UK opportunity is an actionable shortage."""


@app.command()
def analyse(
    asin: Annotated[str, typer.Option(help="Amazon product ID to analyse.")],
    marketplace: Annotated[str, typer.Option(help="Amazon marketplace.")] = "UK",
) -> None:
    """Analyse one product. Placeholder: no data is fetched yet."""
    typer.echo(f"Not implemented yet: would analyse {asin} on {marketplace}.")
