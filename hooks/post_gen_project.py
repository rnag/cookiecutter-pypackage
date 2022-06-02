#!/usr/bin/env python
import os
import shutil
from subprocess import Popen

# Get the root project directory
PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filename):
    """
    generic remove file from project dir
    """
    fullpath = os.path.join(PROJECT_DIRECTORY, filename)
    if os.path.exists(fullpath):
        os.remove(fullpath)


def remove_dir(filename):
    """
    generic remove folder (directory) from project dir
    """
    fullpath = os.path.join(PROJECT_DIRECTORY, filename)
    if os.path.exists(fullpath):
        shutil.rmtree(fullpath)


def init_git():
    """
    Initializes git on the new project folder
    """
    GIT_COMMANDS = [
        ["git", "init"],
        ["git", "add", "."],
        ["git", "commit", "-a", "-m", "Initial Commit"]
    ]

    for command in GIT_COMMANDS:
        git = Popen(command, cwd=PROJECT_DIRECTORY)
        git.wait()


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

    # Remove unused ci choice
    if '{{ cookiecutter.use_ci}}'.lower() != 'gh-actions':
        remove_dir(".github")

    if 'y' != '{{ cookiecutter.add_pyup_badge|lower }}':
        remove_file('.pyup.yml')

    # Initialize Git (should be run after all file have been modified or deleted)
    init_git()
