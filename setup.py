#!/usr/bin/env python

# Copyright (c) 2018 Red Hat, Inc.
# All Rights Reserved.

from setuptools import setup, find_packages

setup(
    name="ansible-connect",
    version="0.0.0",
    author="Peter Sprygada (@privateip)",
    url="https://github.com/nmake/ansible-connect",
    packages=find_packages(),
    install_requires=[
        'ansible'
    ],
    zip_safe=False,
    entry_points={
        'console_scripts': [
            'ansible-connect = ansible_connect.__main__:run'
        ]
    }
)
