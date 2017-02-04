# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='HomeLightSystem',
    version='0.1.0',
    description='Home Lighting System',
    long_description=readme,
    author='AJ9',
    author_email='contact@aj9.co.uk',
    url='https://github.com/aj9/HomeLightSystem',
    license=license,
    install_requires=['nose'],
    packages=find_packages(exclude=('tests', 'docs'))
)

