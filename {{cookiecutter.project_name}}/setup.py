"""
setup.py - config
"""
from codecs import open
from os import path
from setuptools import setup, find_packages

here = path.abspath(path.dirname(__file__))

with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='{{cookiecutter.package_name}}',
    version='{{cookiecutter.version}}',
    install_requires=required,
    description='{{cookiecutter.description}}',
    long_description=long_description,
    author='{{cookiecutter.author}}',
    license='{{cookiecutter.license}}',
    classifiers=[

        'Programming Language :: Python :: 3.5',
    ],
    packages=find_packages(exclude=['contrib', 'docs', 'tests']),

    # entry_points={
    #    'console_scripts': [
    #        'sample=sample:main',
    #    ],
    # },
)
