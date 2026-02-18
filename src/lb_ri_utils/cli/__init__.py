"""CLI for lb-ri-utils."""

import typer

app = typer.Typer(
    name="lb_ri_utils",
    help="Utilities for working with radio interfermetric data",
    no_args_is_help=True,
)


@app.callback()
def callback() -> None:
    """Utilities for working with radio interfermetric data"""
    pass


# Register subcommands below. Imports go here (bottom) to avoid circular imports.
from lb_ri_utils.cli.onboard import onboard  # noqa: E402

app.command(name="onboard")(onboard)

__all__ = ["app"]
