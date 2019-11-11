from distutils.core import setup, Extension
from Cython.Build import cythonize

# First create an Extension object with the appropriate name and sources.
ext = Extension(name="fib", sources=["cfib.c", "fib.pyx"])

# Use cythonize on the extension object.
setup(ext_modules=cythonize(ext))