#!/usr/bin/env python
from numpy.distutils.core import Extension, setup
import os
import shlex

VERSION = '0.2.0'

with open('README.rst') as f:
    README = f.read()
DESCRIPTION = README.split('\n')[2]
LONG_DESCRIPTION = '\n'.join(README.split('\n')[17:])


# https://groups.google.com/a/continuum.io/forum/#!topic/anaconda/Xw57CjIcBIU
# https://github.com/numpy/numpy/issues/1171

ldflags = os.environ.get('LDFLAGS', '')
if ldflags == '':
    extra_link_args = None
else:
    extra_link_args = ["-shared"] + shlex.split(ldflags)

EXT = Extension(name='toeplitz',
                sources=['src/toeplitz.pyf', 'src/toeplitz.f90'],
                extra_link_args=extra_link_args)

CLASSIFIERS = [
    'Environment :: Console',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Scientific/Engineering :: Mathematics'
    ]

setup(name='toeplitz',
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author='Tom Eulenfeld',
      author_email='tom.eulenfeld@gmail.com',
      license='MIT',
      url='https://github.com/trichter/toeplitz',
      classifiers=CLASSIFIERS,
      ext_modules=[EXT],
      scripts=['scripts/toeplitz-runtests'],
      requires=['numpy'],
      include_package_data=True
      )
