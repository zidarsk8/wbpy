#!/usr/bin/env python3

"""Wbpy setup file.

This is the main setup for wbpy. To manually install this module run:

    python setup.py install

for developer to keep track of the changes in the module run:

    python setup.py develop
"""

import re
from setuptools import setup

INIT_PY = open("wbpy/__init__.py").read()
METADATA = dict(re.findall("__([a-z]+)__ = \"([^\"]+)\"", INIT_PY))


setup(
    name=METADATA["name"],
    version=METADATA["version"],
    license=METADATA["license"],
    author="Matthew Duck",
    author_email=METADATA["email"],
    description=("A Python interface to the World Bank Indicators and Climate"
                 "APIs"),
    long_description=open('README.rst').read(),
    url="https://github.com/zidarsk8/wbpy",
    packages=['wbpy', 'wbpy.tests'],
    provides=['wbpy'],
    package_data={"wbpy": ["non_ISO_region_codes.json"]},
    install_requires=["pycountry"],
    tests_require=["tox"],
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Scientific/Engineering',
    ],
)
