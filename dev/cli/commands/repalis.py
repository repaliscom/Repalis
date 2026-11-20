"""Run the Repalis CLI from source in the current directory."""

import os

import typer

from shared import CLIENTS_DIR, check_command_exists, console

CLI_ENTRY = CLIENTS_DIR / "packages" / "cli" / "src" / "cli.ts"


def register(app: typer.Typer, prompt_setup: callable) -> None:
    @app.command(
        name="repalis",
        add_help_option=False,
        context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
    )
    @app.command(
        name="repalis",
        add_help_option=False,
        context_settings={"allow_extra_args": True, "ignore_unknown_options": True},
    )
    def repalis(ctx: typer.Context) -> None:
        """Run the Repalis CLI from source in the current directory.

        Examples:
          dev repalis auth login --local
          dev repalis config plan
        """
        if not check_command_exists("bun"):
            console.print("[red]bun not found. Install it from https://bun.sh[/red]")
            raise typer.Exit(1)
        cmd = ["bun", "--no-env-file", str(CLI_ENTRY), *ctx.args]
        os.execvpe(cmd[0], cmd, {**os.environ, "POLAR_PREVIEW": "1"})
