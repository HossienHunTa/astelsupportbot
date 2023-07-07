#!/usr/bin/env python

from astelbot import __version__

try:
    from setuptools import find_packages, setup
except ImportError:
    from distutils.core import setup


install_requires = [
    "aiohttp==3.8.4"
    "aiosignal==1.3.1"
    "async-timeout==4.0.2"
    "attrs==23.1.0"
    "certifi==2023.5.7"
    "cfgv==3.3.1"
    "charset-normalizer==3.1.0"
    "distlib==0.3.6"
    "filelock==3.12.2"
    "frozenlist==1.3.3"
    "identify==2.5.24"
    "idna==3.4"
    "multidict==6.0.4"
    "nodeenv==1.8.0"
    "platformdirs==3.8.1"
    "pre-commit==3.3.3"
    "pyaes==1.6.1"
    "Pyrogram==2.0.106"
    "PySocks==1.7.1"
    "python-dotenv==1.0.0"
    "PyYAML==6.0"
    "requests==2.31.0"
    "ruff==0.0.277"
    "telegraph==2.2.0"
    "TgCrypto==1.2.5"
    "urllib3==2.0.3"
    "virtualenv==20.23.1"
    "yarl==1.9.2"
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
