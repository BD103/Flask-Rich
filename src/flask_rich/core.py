import logging
from rich.logging import RichHandler


class RichApplication(object):
    def __init__(self, app=None, enable_logging: bool=True, logging_markup: bool=True):
        self.app = app
        self.enable_logging = enable_logging
        self.logging_markup = logging_markup

        if app is not None:
            self.init_app(app)
    
    def init_app(self, app):
        if self.enable_logging:
            logging.basicConfig(
                level="NOTSET", format="%(message)s", datefmt="[%X]", handlers=[RichHandler(markup=self.logging_markup)]
            )
