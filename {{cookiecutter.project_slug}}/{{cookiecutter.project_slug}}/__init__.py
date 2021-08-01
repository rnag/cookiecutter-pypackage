"""
{{ cookiecutter.project_short_description }}


Docs:
    - https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io/en/latest/

"""
__all__ = [

]

import logging

# Set up logging to ``/dev/null`` like a library is supposed to.
# http://docs.python.org/3.3/howto/logging.html#configuring-logging-for-a-library
logging.getLogger('{{ cookiecutter.project_slug }}').addHandler(logging.NullHandler())
