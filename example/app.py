from flask import Flask
from flask_rich import RichApplication


app = Flask(__name__)
rich = RichApplication(app)

app.logger.debug("If this is [red]colorful[/red], everything worked!")
app.logger.debug("1, 2.4, True, False, None")
