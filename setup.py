#!/usr/bin/env python
"""Setup logic for pip."""

from setuptools import setup

setup(
    name='automata_python',
    version='0.0.1',
    description='Python Automata Library',
    url='https://github.com/AbhishekKumarSingh00/automata-python',
    author='Abhishek Kumar Singh and Abhishek Midha',
    author_email='abhishek.kumar.singh2101@gmail.com',
    license='GPLv3',
    keywords='language finite automata turing machine push down automata linear bound automata',
    packages=[
        'automata'
    ],
    install_requires=[],
    entry_points={}
)
