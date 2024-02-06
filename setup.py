import re
from setuptools import setup
from setuptools import Extension

try:
    from Cython.Build import cythonize
except ImportError:
    USE_CYTHON = False
else:
    USE_CYTHON = True


def find_version():
    return re.search(r"^__version__ = '(.*)'$",
                     open('heatshrink2/version.py', 'r').read(),
                     re.MULTILINE).group(1)


# Compiled file extension to use. If we're not using Cython,
# just use the plain C file.
EXT = '.pyx' if USE_CYTHON else '.c'

heatshrink_module = Extension('heatshrink2.core',
                              include_dirs=[
                                  'heatshrink2/_heatshrink'
                              ],
                              sources=[
                                  'heatshrink2/core' + EXT,
                                  'heatshrink2/_heatshrink/heatshrink_encoder.c',
                                  'heatshrink2/_heatshrink/heatshrink_decoder.c'
                              ])

if USE_CYTHON:
    extensions = cythonize([heatshrink_module], compiler_directives={"language_level": "2"})
else:
    extensions = [heatshrink_module]

setup(name='heatshrink2',
      version=find_version(),
      author='Antonis Kalou @ JOHAN Sports, Erik Moqvist',
      author_email='antonis@johan-sports.com, erik.moqvist@gmail.com',
      description='Python bindings to the heatshrink library',
      long_description=open('README.rst', 'r').read(),
      url='https://github.com/eerimoq/pyheatshrink',
      license='ISC',
      classifiers=[
          'Programming Language :: Python :: 3'
      ],
      keywords='compression binding heatshrink LZSS',
      test_suite='tests',
      packages=['heatshrink2'],
      ext_modules=extensions)
