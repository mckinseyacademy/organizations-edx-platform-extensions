#!/usr/bin/env python

from setuptools import find_packages, setup

setup(
    name='organizations-edx-platform-extensions',
    version='3.0.2',
    description='Organization management extension for edX platform',
    long_description=open('README.rst').read(),
    author='edX',
    url='https://github.com/edx-solutions/organizations-edx-platform-extensions.git',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "Django>=2.2,<2.3",
    ],
)
