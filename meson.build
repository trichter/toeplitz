project('toeplitz', 'c',
  version : '0.3.5',
  meson_version: '>=0.64.0',
  default_options : ['warning_level=2'],
)

add_languages('fortran')
py_mod = import('python')
py = py_mod.find_installation(pure: false)
py_dep = py.dependency()

incdir_numpy = run_command(py,
  ['-c', 'import os; os.chdir(".."); import numpy; print(numpy.get_include())'],
  check : true
).stdout().strip()

incdir_f2py = run_command(py,
    ['-c', 'import os; os.chdir(".."); import numpy.f2py; print(numpy.f2py.get_include())'],
    check : true
).stdout().strip()

toeplitz_source = custom_target('toeplitzmodule.c',
  input : ['src/toeplitz.pyf', 'src/toeplitz.f90'],
  output : ['toeplitzmodule.c', 'toeplitz-f2pywrappers.f'],
  command : [py, '-m', 'numpy.f2py', '@INPUT@', '-m', 'toeplitz']
)

inc_np = include_directories(incdir_numpy, incdir_f2py)

py.extension_module('toeplitz',
  ['src/toeplitz.f90', toeplitz_source],
  #[toeplitz_source],
  incdir_f2py / 'fortranobject.c',
  fortran_args: '-fallow-argument-mismatch',
  include_directories: inc_np,
  dependencies : py_dep,
  install : true
)
