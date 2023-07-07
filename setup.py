#!/usr/bin/env python

from astelbot import __version__

try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import setup


install_requires = [

]

setup(
    name="astelbot",
    version=__version__,
    description="A Telegram bot to help Astel support department.",
    author="Hossien Mohmmadain",
    author_email="hossien021.m@yahoo.com",
    url="https://astel.ir",
    project_urls={
        "Source": "https://github.com/astelsupportbot/astelbot",
    },
    packages=find_packages(),
    include_package_data=True,
    license="MIT",
    python_requires=">=3.9",
    install_requires=install_requires,
)