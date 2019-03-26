#!/usr/bin/env python
#coding=utf8

try:
    from  setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
        name = 'pyproxy',
        version = '1.0',
        install_requires = [], 
        description = 'python proxy server',
        url = 'https://github.com/zhouxianggen/pyproxy', 
        author = 'zhouxianggen',
        author_email = 'zhouxianggen@gmail.com',
        classifiers = [ 'Programming Language :: Python :: 3.7',],
        packages = ['pyproxy'],
        data_files = [ ], 
        )

