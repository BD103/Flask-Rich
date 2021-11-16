import logging
from rich.logging import RichHandler


class RichApplication(object):
    def __init__(self, app=None):
        self.app = app

        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        defaults = [
            ("RICH_LOGGING", True),
            ("RICH_LOGGING_MARKUP", True)
        ]

        for k, v in defaults:
            app.config.setdefault(k, v)

        if app.config["RICH_LOGGING"]:
            logging.basicConfig(
                level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler(markup=app.config["RICH_LOGGING_MARKUP"])]
            )
