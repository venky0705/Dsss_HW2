from distutils.core import setup
from setuptools import find_packages

setup(
    name="mathquiz",
    version="0.1",
    author="sgupta",
    author_email="shubham.g.gupta@fau.de",
    packages=find_packages(),
    install_requires=["numpy"],
)