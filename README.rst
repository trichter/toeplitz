toeplitz
========
Python wrapper for Fortran90 toeplitz package to solve a variety of Toeplitz and circulant linear systems
---------------------------------------------------------------------------------------------------------

|buildstatus| |version| |pyversions|

.. |buildstatus| image:: https://api.travis-ci.org/trichter/toeplitz.svg?
    branch=master
   :target: https://travis-ci.org/trichter/toeplitz

.. |version| image:: https://img.shields.io/pypi/v/toeplitz.svg
   :target: https://pypi.python.org/pypi/toeplitz

.. |pyversions| image:: https://img.shields.io/pypi/pyversions/toeplitz.svg
   :target: https://python.org

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

Installation
------------

Toeplitz can be installed with the command ``pip toeplitz``. To install toeplitz into a fresh conda environment run::

    conda create -n toeplenv numpy scipy gfortran_linux-64
    conda activate toeplenv
    pip install toeplitz
    toeplitz-runtests

For OSX the package ``gfortran_osx-64`` must be used instead of ``gfortran_linux-64``.
For Windows you need to install the FORTRAN compiler yourself (MinGW).

.. _John Burkhardt's website: http://people.sc.fsu.edu/~jburkardt/f_src/toeplitz/toeplitz.html
.. _NumPy: http://www.numpy.org/
.. _pip: http://www.pip-installer.org/