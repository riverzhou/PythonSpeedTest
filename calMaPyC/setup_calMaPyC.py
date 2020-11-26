#!/usr/bin/env python3

from distutils.core import setup, Extension
import numpy

calMaPyC_module = Extension(
    'calMaPyCG',
    sources=['calMaPyC.cpp'],
    language='c',
    include_dirs=[numpy.get_include()],
    library_dirs=['D:\Anaconda3'],
    libraries=[],
    extra_compile_args=['-O3','-DNDEBUG'],
    extra_link_args=[]
)

setup(ext_modules=[calMaPyC_module])

