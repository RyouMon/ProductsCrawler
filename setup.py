from setuptools import setup

with open('requirements.txt') as f:
    requires = [line.rstrip() for line in f.readlines()]

setup(install_requires=requires)
