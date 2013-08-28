#!/usr/bin/env python

from numpy.distutils.core import Extension, setup

ext = Extension(name = 'toeplitz',
                sources = ['src/toeplitz.pyf', 'src/toeplitz.f90'])

setup(name = 'toeplitz',
      description = 'Wrapper for fortran 90 toeplitz package',
      author = 'Tom Richter',
      url = 'https://github.com/trichter/toeplitz',
      ext_modules = [ext],
      scripts=['scripts/toeplitz-runtests'],
      provides=['toeplitz'],
      requires=['numpy'],
      license='MIT license'
      )
