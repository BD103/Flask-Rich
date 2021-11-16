import logging

from rich.logging import RichHandler
from rich.traceback import install as install_traceback


class RichApplication(object):
    def __init__(self, app=None):
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        defaults = [
            ("RICH_LOGGING", True),
            ("RICH_LOGGING_MARKUP", True),
            ("RICH_TRACEBACK", True),
            ("RICH_TRACEBACK_EXTRA_LINES", 1),
            ("RICH_TRACEBACK_SHOW_LOCALS", False),
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
