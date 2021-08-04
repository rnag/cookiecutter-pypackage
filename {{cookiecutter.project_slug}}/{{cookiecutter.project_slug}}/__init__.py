{%- set license_metadata = {
    'MIT license': 'MIT',
    'Apache Software License 2.0': 'Apache 2.0'
} -%}
"""
{{ cookiecutter.project_name }}
{{ '~' * cookiecutter.project_slug | length }}

{{ cookiecutter.project_short_description }}

Sample Usage:

    >>> import {{ cookiecutter.project_slug }}

For full documentation and more advanced usage, please see
<https://{{ cookiecutter.project_slug | replace("_", "-") }}.readthedocs.io>.

:copyright: (c) {% now 'local', '%Y' %} by {{ cookiecutter.full_name }}.
:license:
{%- if cookiecutter.open_source_license in license_metadata -%}
 {{ license_metadata[cookiecutter.open_source_license] }}
{%- else -%}
 {{ cookiecutter.open_source_license.split(" ", 1)[0] }}
{%- endif -%}
, see LICENSE for more details.
"""

__all__ = [

]

import logging


# Set up logging to ``/dev/null`` like a library is supposed to.
# http://docs.python.org/3.3/howto/logging.html#configuring-logging-for-a-library
logging.getLogger('{{ cookiecutter.project_slug }}').addHandler(logging.NullHandler())
