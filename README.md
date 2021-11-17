# Flask Rich

Implements the [Rich](https://pypi.org/project/rich/) programming library with [Flask](https://pypi.org/project/Flask/). All features are toggleable, including:

- Better logging
- Colorful tracebacks
- Better `routes` command

## Usage

Import the `RichApplication` class.

```python
from flask_rich import RichApplication
from flask import Flask

rich = RichApplication()

app = Flask(__name__)
app.config["RICH_EXAMPLE_SETTING"] = "value"

rich.init_app(app)

# Or
# rich = RichApplication(app)
```

### Class options

#### `RICH_LOGGING: bool = True`

Whether to use [Rich's logging](https://rich.readthedocs.io/en/latest/logging.html) handler.

#### `RICH_LOGGING_MARKUP: bool = True`

Whether to allow [Rich's console markup](https://rich.readthedocs.io/en/latest/markup.html#console-markup) format in logging.

An example of console markup is `[blue]Hello[/blue], world!`.

#### `RICH_TRACEBACK: bool = True`

Whether to use [Rich's traceback](https://rich.readthedocs.io/en/latest/traceback.html) handler.

#### `RICH_TRACEBACK_EXTRA_LINES: int = 1`

When Rich prints the lines of code which raised the error, how many lines around it does it print as well. In the library it defaults to 3, but 1 is better for web applications.

#### `RICH_TRACEBACK_SHOW_LOCALS: bool = False`

Whether to print the local variables with traceback.

#### `RICH_ROUTES: bool = True`

Whether to add a new command that uses [Rich's tables](https://rich.readthedocs.io/en/latest/tables.html) to show all routes. (Activate with `flask rich-routes`.)

#### `RICH_ROUTES_MODE: str = "table"`

What mode the command is in. There is only one option: table.

## Contributing

PRs are welcome! You can setup your own copy of the source code with:

```shell
# Git
git clone https://github.com/BD103/Flask-Rich.git
cd Flask-Rich/

# Poetry
poetry lock
poetry install
poetry shell
```

You will need [Poetry](https://python-poetry.org/) for managing dependencies.