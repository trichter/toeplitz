#!/usr/bin/env python
from numpy.distutils.core import Extension, setup

VERSION='0.1.4'

with open('README.rst') as f:
    README = f.read()
DESCRIPTION = README.split('\n')[2]
LONG_DESCRIPTION = '\n'.join(README.split('\n')[17:])

EXT = Extension(name='toeplitz',
                sources=['src/toeplitz.pyf', 'src/toeplitz.f90'])

CLASSIFIERS = [
    'Environment :: Console',
    'Intended Audience :: Science/Research',
    'License :: OSI Approved :: MIT License',
    'Operating System :: OS Independent',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.3',
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
