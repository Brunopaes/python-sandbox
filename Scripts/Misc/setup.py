from setuptools import setup, Extension, Command
from Cython.Build import cythonize


setup(ext_modules=cythonize('elo_classifier.pyx'))
