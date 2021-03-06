#!/usr/bin/env python
# coding=utf-8

from setuptools import setup, find_packages

setup(
    name='navinfo_tool',
    version='0.0.2',
    description=(
        'utils for nlp'
    ),
    author='liyuhao',
    author_email='1241225413@qq.com',
    license='Apache License 2.0',
    packages=find_packages(),
    url='https://github.com/hgliyuhao/little_dinosaur',
    install_requires=[
        'xlrd==1.2.0',
        'jieba',
        'xlwt',
        'xlutils',
        'matplotlib',
        'sklearn',
        'pandas',
        'fairies'
    ],
)
