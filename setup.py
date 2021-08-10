#!/usr/bin/env python

from setuptools import setup

setup(
    name = 'FOFA_PY3',
    version = '1.0.0',
    description = 'Python library for FOFA (https://fofa.so)',
    author = 'lanvnal',
    author_email = 'xxx@xxx.com',
    url = 'xxx',
    packages = ['fofa_py3', 'fofa_py3.poc', 'fofa_py3.src'],
    classifiers = [
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)