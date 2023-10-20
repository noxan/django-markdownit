# django-markdown-it

Markdown template filter for Django following [CommonMark](https://commonmark.org/) specs and using [markdown-it-py](https://github.com/executablebooks/markdown-it-py) under the hood.

## Installation

1. Install the package:

    ```bash
    poetry add django-markdown-it
    ```
    or using pip:
    ```bash
    pip install django-markdown-it
    ```

2. Add `markdownit` to your `INSTALLED_APPS`:

    ```python
    INSTALLED_APPS = [
        # ...
        'markdownit',
    ]
    ```

## Usage

1. Load the template tag library in your template:

    ```django
    {% load markdownit %}
    ```

2. Use the `markdownit` filter on a string:

    ```django
    {{ my_string|markdownit }}
    ```


## Credits

Inspired by [django-markdownify](https://github.com/erwinmatijsen/django-markdownify/).
