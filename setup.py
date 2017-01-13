#!/usr/bin/env python

# NOTE: This package must support Python 2.7 in addition to Python 3.x

from distutils.core import setup

version = '0.1.0'
description = 'Experimental type system extensions for programs checked with the mypy typechecker.'
long_description = '''
Mypy Extensions
===============

The "mypy_extensions" module defines experimental extensions to the
standard "typing" module that are supported by the mypy typechecker.
'''.lstrip()

classifiers = [
    'Development Status :: 2 - Pre-Alpha',
    'Environment :: Console',
    'Intended Audience :: Developers',
    'License :: OSI Approved :: MIT License',
    'Operating System :: POSIX',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Software Development',
]

setup(
    name='mypy_extensions',
    version=version,
    description=description,
    long_description=long_description,
    author='David Foster',
    author_email='david@dafoster.net',
    url='http://www.mypy-lang.org/',
    license='MIT License',
    platforms=['POSIX'],
    py_modules=['mypy_extensions'],
    classifiers=classifiers,
)
