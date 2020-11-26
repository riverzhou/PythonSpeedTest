#!/usr/bin/env python3

from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

setup(ext_modules = cythonize(Extension(
    'calMaCY',
    sources=['calMaCY.pyx'],
    language='c',
    include_dirs=[numpy.get_include()],
    library_dirs=['D:\Anaconda3'],
    libraries=[],
    extra_compile_args=['-O3','-DNDEBUG'],
    extra_link_args=[]
)))

