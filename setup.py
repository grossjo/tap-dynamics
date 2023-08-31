#!/usr/bin/env python

from setuptools import setup

setup(
    name="tap-dynamics",
    version="0.1.4",
    description="Singer.io tap for extracting data from the Microsoft Dynamics 365 API",
    classifiers=["Programming Language :: Python :: 3 :: Only"],
    install_requires=[
        "requests==2.29.0",
        "singer-python==5.8.1",
        "odata @ https://github.com/dreamdata-io/python-odata/archive/master.zip",
    ],
    entry_points="""
          [console_scripts]
          tap-dynamics=tap_dynamics:main
      """,
    packages=["tap_dynamics"],
)
