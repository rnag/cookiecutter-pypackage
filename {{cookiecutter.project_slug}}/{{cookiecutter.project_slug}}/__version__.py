{%- set license_metadata = {
    'MIT license': 'MIT',
    'Apache Software License 2.0': 'Apache 2.0'
} -%}
"""
{{ cookiecutter.project_name }} - {{ cookiecutter.project_short_description }}
"""

__title__ = '{{ cookiecutter.project_slug | replace("_", "-") }}'
__description__ = '{{ cookiecutter.project_short_description }}'
__url__ = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug | replace("_", "-") }}'
__version__ = '{{ cookiecutter.version }}'
__author__ = '{{ cookiecutter.full_name }}'
__author_email__ = '{{ cookiecutter.email }}'
{%- if cookiecutter.open_source_license in license_metadata %}
__license__ = '{{ license_metadata[cookiecutter.open_source_license] }}'
{%- else %}
__license__ = '{{ cookiecutter.open_source_license.split(" ", 1)[0] }}'
{%- endif %}
__copyright__ = 'Copyright {% now "local", "%Y" %} {{ cookiecutter.full_name }}'
