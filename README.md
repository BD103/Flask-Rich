# Flask Rich

Implements the [Rich](https://pypi.org/project/rich/) programming library with [Flask](https://pypi.org/project/Flask/). All features are toggleable, including:

- Better logging

## Usage

Import the `RichApplication` class.

```python
from flask_rich import RichApplication
from flask import Flask

rich = RichApplication()

app = Flask(__name__)
rich.init_app(app)

# Or
# rich = RichApplication(app)
```

### Class options

#### `app = None`

The Flask app that is used. It is optional, but you need to call `RichApplication.init_app(app)` later to enabled to library.

app=None, enable_logging: bool=True, logging_markup: bool=True

#### `enable_logging: bool = True`

Whether to use [Rich's logging](https://rich.readthedocs.io/en/latest/logging.html) handler.

#### `logging_markup: bool = True`

Whether to allow [Rich's console markup](https://rich.readthedocs.io/en/latest/markup.html#console-markup) format in logging.

An example of console markup is `[blue]Hello[/blue], world!`.

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