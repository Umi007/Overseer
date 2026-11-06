from typer.testing import CliRunner

from overseer.cli import app

runner = CliRunner()


def test_analyse_echoes_asin_and_default_marketplace():
    result = runner.invoke(app, ["analyse", "--asin", "B0EXAMPLE1"])

    assert result.exit_code == 0
    assert "B0EXAMPLE1" in result.output
    assert "UK" in result.output


def test_analyse_requires_asin():
    result = runner.invoke(app, ["analyse"])

    assert result.exit_code != 0
