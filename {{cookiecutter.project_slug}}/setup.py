"""The setup script."""
import pathlib

from setuptools import setup, find_packages


here = pathlib.Path(__file__).parent

package_name = '{{ cookiecutter.project_slug }}'

packages = find_packages(include=[package_name, f'{package_name}.*'])

requires = [{%- if cookiecutter.command_line_interface|lower == 'click' %}'Click>=7.0',{%- endif %} ]

test_requirements = [{%- if cookiecutter.use_pytest == 'y' %}'pytest-cov>=2.10.0',{%- endif %} ]

about = {}
exec((here / package_name / '__version__.py').read_text(), about)

readme = (here / 'README.rst').read_text()
history = (here / 'HISTORY.rst').read_text()

{%- set license_classifiers = {
    'MIT license': 'License :: OSI Approved :: MIT License',
    'BSD license': 'License :: OSI Approved :: BSD License',
    'ISC license': 'License :: OSI Approved :: ISC License (ISCL)',
    'Apache Software License 2.0': 'License :: OSI Approved :: Apache Software License',
    'GNU General Public License v3': 'License :: OSI Approved :: GNU General Public License v3 (GPLv3)'
} %}

setup(
    name=about['__title__'],
    version=about['__version__'],
    description=about['__description__'],
    long_description=readme + '\n\n' + history,
    author=about['__author__'],
    author_email=about['__author_email__'],
    url=about['__url__'],
    packages=packages,
    include_package_data=True,
    install_requires=requires,
{%- if cookiecutter.open_source_license in license_classifiers %}
    license=about['__license__'],
{%- endif %}
    # TODO add more relevant keywords as needed
    keywords=['{{ cookiecutter.project_slug | replace("_", "-") }}'],
    classifiers=[
        # Ref: https://pypi.org/classifiers/
        # 'Development Status :: 5 - Production/Stable',
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
{%- if cookiecutter.open_source_license in license_classifiers %}
        '{{ license_classifiers[cookiecutter.open_source_license] }}',
{%- endif %}
        'Natural Language :: English',
        'Programming Language :: Python :: 3 :: Only',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python'
],
    {%- if 'no' not in cookiecutter.command_line_interface|lower %}
    python_requires = '>=3.6',
    entry_points={
        'console_scripts': [
            '{{ cookiecutter.project_slug | replace("_", "-") }}={{ cookiecutter.project_slug }}.cli:main',
        ],
    },
    {%- endif %}
    test_suite='tests',
    tests_require=test_requirements,
    zip_safe=False
)
