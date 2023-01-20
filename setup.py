#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import find_packages, setup

setup(
    include_package_data=True,
    name='lona-picocss',
    version='0.0',
    author='Florian Scherf',
    url='https://github.com/lona-web-org/lona-picocss',
    author_email='mail@florianscherf.de',
    license='MIT',
    packages=find_packages(),
    install_requires=[
        'lona>=1.10.5',
    ],
    scripts=[],
    entry_points={},
)
