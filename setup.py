#!/usr/bin/env python

"""The setup script."""

import codecs
import os
import re

from setuptools import setup, find_packages


with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('docs/HISTORY.rst') as history_file:
    history = history_file.read()

requirements = "" 

setup(
    name="uv.hdp",
    author="UV WEB Community",
    author_email="ck@novareto.de",
    version="0.1.0",
    description="SOAP-Service Calls to HDP-Web-Service",
    long_description=readme + '\n\n' + history,
    long_description_content_type="text/x-rst",
    url="https://git.bg-kooperation.de",
    include_package_data=True,
    packages=find_packages(include=['uv.hdp']),
    install_requires=[
        'zeep',
        'uv.models'
        ],
    test_suite='tests',
    zip_safe=False,
)
