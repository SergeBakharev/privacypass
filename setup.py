#!/usr/bin/env python3
# coding: utf-8

"""
    PrivacyPass
"""
import configparser

from setuptools import find_packages, setup  # noqa: H301

NAME = "privacypass"
# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools

# Converting Pipfile to requirements style list because setup expects requirements.txt file.
parser = configparser.ConfigParser()
parser.read("Pipfile")
install_requires = [f'{key}{value}'.replace('\"', '').replace('*', '') for key, value in parser['packages'].items()]

with open('README.md', 'r') as f:
    readme = f.read()

setup(
    use_scm_version={
        'local_scheme': lambda a: ""
    },
    setup_requires=['setuptools_scm'],
    name=NAME,
    description="Bypass Cloudflare's CAPTCHAs by redeming Privacy Pass tokens.",
    author_email="",
    url="https://github.com/sergebakharev/privacypass",
    keywords=["cloudflare", "captcha", 'scraping'],
    install_requires=install_requires,
    packages=find_packages(),
    include_package_data=True,
    long_description=readme,
    long_description_content_type='text/markdown',
    license='MIT',
    classifiers=[
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.9',
    ],
    python_requires=">=3.9",
    author="Serge Bakharev"
)
