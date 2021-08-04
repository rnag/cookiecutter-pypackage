#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':

    if '{{ cookiecutter.create_author_file }}' != 'y':
        remove_file('AUTHORS.rst')
        remove_file('docs/authors.rst')

    if 'no' in '{{ cookiecutter.command_line_interface|lower }}':
        cli_file = os.path.join('{{ cookiecutter.project_slug }}', 'cli.py')
        remove_file(cli_file)

    if 'Not open source' == '{{ cookiecutter.open_source_license }}':
        remove_file('LICENSE')

    if 'y' != '{{ cookiecutter.use_pytest|lower }}':
        remove_file('pytest.ini')

    if 'y' != '{{ cookiecutter.use_pypi_deployment_with_travis|lower }}':
        remove_file('.travis.yml')

    if 'y' != '{{ cookiecutter.add_pyup_badge|lower }}':
        remove_file('.pyup.yml')
