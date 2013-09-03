#!/usr/bin/env python
"""
toeplitz
========
Python wrapper for Fortran90 toeplitz package to solve a variety of Toeplitz and circulant linear systems
---------------------------------------------------------------------------------------------------------

The wrapped Fortran90 toeplitz package was written by John Burkardt and is distributed under GNU LGPL license.
It can be obtained from `John Burkhardt's website`_.
There you can additionally find a short documentation and the following description:

``TOEPLITZ is a FORTRAN90 library which solves a variety of Toeplitz and circulant linear systems.
The package can also handle circulant Toeplitz systems, and some other more complicated but related forms.
The TOEPLITZ package was written in the early 1980's by a joint working group of American and Soviet mathematicians.
The original, true, correct version of TOEPLITZ is available in the TOEPLITZ subdirectory of the NETLIB web site.``

This wrapper is based on numpy/f2py and provides a python interface for all fortran subroutines \*_sl.
Only the functions sto_sl and cto_sl (solve linear Toeplitz systems) are tested.
They provide acceptable accuracy compared to scipy.linalg and run faster for large inputs.
All other routines are not tested, but should work.
For more documentation than on John Burkardt's website check the source file toeplitz.f90.

.. _John Burkhardt's website: http://people.sc.fsu.edu/~jburkardt/f_src/toeplitz/toeplitz.html
"""


from numpy.distutils.core import Extension, setup

ext = Extension(name='toeplitz',
                sources=['src/toeplitz.pyf', 'src/toeplitz.f90'])

setup(name='toeplitz',
      version='0.1',
      description='Wrapper for fortran 90 toeplitz package',
      long_description=__doc__,
      author='Tom Richter',
      author_email='richter@gfz-potsdam.de',
      license='MIT license',
      url='https://github.com/trichter/toeplitz',
      ext_modules=[ext],
      scripts=['scripts/toeplitz-runtests'],
      requires=['numpy']
      )
