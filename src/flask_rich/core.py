import logging
from operator import attrgetter

import click
from rich.console import Console
from rich.logging import RichHandler
from rich.table import Column, Table
from rich.traceback import install as install_traceback


class RichApplication(object):
    def __init__(self, app=None):
        self.app = app
        self.console = Console()

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        defaults = [
            ("RICH_LOGGING", True),
            ("RICH_LOGGING_MARKUP", True),
            ("RICH_TRACEBACK", True),
            ("RICH_TRACEBACK_EXTRA_LINES", 1),
            ("RICH_TRACEBACK_SHOW_LOCALS", False),
            ("RICH_ROUTES", True),
            ("RICH_ROUTES_MODE", "table"),
        ]

        for k, v in defaults:
            app.config.setdefault(k, v)

        if app.config["RICH_LOGGING"]:
            logging.basicConfig(
                level="NOTSET",
                format="%(message)s",
                datefmt="[%X]",
                handlers=[RichHandler(markup=app.config["RICH_LOGGING_MARKUP"])],
            )

        if app.config["RICH_TRACEBACK"]:
            install_traceback(
                extra_lines=app.config["RICH_TRACEBACK_EXTRA_LINES"],
                show_locals=app.config["RICH_TRACEBACK_SHOW_LOCALS"],
            )

        if app.config["RICH_ROUTES"]:
            if app.config["RICH_ROUTES_MODE"] == "table":

                @app.cli.command(
                    "rich-routes", short_help="Show the routes for the app."
                )
                @click.option(
                    "--all-methods", is_flag=True, help="Show HEAD and OPTIONS methods."
                )
                def rich_routes_command(all_methods: bool) -> None:
                    rules = list(app.url_map.iter_rules())

                    if not rules:
                        click.echo("No routes were registered.")
                        return

                    ignored_methods = set(() if all_methods else ("HEAD", "OPTIONS"))

                    rule_methods = [
                        ", ".join(sorted(rule.methods - ignored_methods))  # type: ignore
                        for rule in rules
                    ]

                    table = Table(
                        Column("Endpoint", style="bright_magenta"),
                        Column("Methods", style="cyan"),
                        Column("Rule", style="green"),
                        title="App Routes",
                    )

                    for rule, methods in zip(rules, rule_methods):
                        table.add_row(rule.endpoint, methods, rule.rule)

                    self.console.print(table)
