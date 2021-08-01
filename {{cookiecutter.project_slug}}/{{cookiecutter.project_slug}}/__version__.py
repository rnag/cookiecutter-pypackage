"""
{{ cookiecutter.project_short_description }}
"""
__title__ = '{{ cookiecutter.project_slug | replace("_", "-") }}'
__description__ = '{{ cookiecutter.project_short_description }}'
__url__ = 'https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.project_slug | replace("_", "-") }}'
__version__ = '{{ cookiecutter.version }}'
__author__ = """{{ cookiecutter.full_name }}"""
__author_email__ = '{{ cookiecutter.email }}'
__license__ = '{{ cookiecutter.open_source_license.split(" ", 1)[0] }}'
__copyright__ = 'Copyright {% now "local", "%Y" %} {{ cookiecutter.full_name }}'
