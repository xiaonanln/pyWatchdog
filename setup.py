import os
from setuptools import setup
from setuptools import Extension

libname = 'pyWatchdog'

setup(
  name = libname,
  version = '0.1.0', 
  author = 'xiaonanln',
  author_email='xiaonanln@gmail.com', 
  packages = [libname],
  package_dir = {libname: 'src/'+libname},
)
