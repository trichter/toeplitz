#!/usr/bin/env python
from numpy.distutils.core import Extension, setup

VERSION='0.1.2'

with open('README.rst') as f:
    README = f.read()
if not 'dev' in VERSION: # get image for correct version from travis-ci
    README = README.replace('branch=master', 'branch=v%s' % VERSION)
DESCRIPTION = README.split('\n')[2]
LONG_DESCRIPTION = '\n'.join(README.split('\n')[5:])

ext = Extension(name='toeplitz',
                sources=['src/toeplitz.pyf', 'src/toeplitz.f90'])

setup(name='toeplitz',
      version=VERSION,
      description=DESCRIPTION,
      long_description=LONG_DESCRIPTION,
      author='Tom Richter',
      author_email='richter@gfz-potsdam.de',
      license='MIT',
      url='https://github.com/trichter/toeplitz',
      ext_modules=[ext],
      scripts=['scripts/toeplitz-runtests'],
      requires=['numpy'],
      include_package_data=True
      )
