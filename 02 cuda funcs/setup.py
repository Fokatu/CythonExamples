from distutils.core import setup, Extension
from Cython.Build import cythonize

# First create an Extension object with the appropriate name and sources.
ext = Extension(name="cuda_runtime", sources=["cuda_runtime.pyx",],
                libraries=["cudart",],

                library_dirs=[r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\lib\x64",
                              r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\bin",],
                include_dirs=[r"C:\Program Files\NVIDIA GPU Computing Toolkit\CUDA\v10.1\include", ])

# Use cythonize on the extension object.
setup(ext_modules=cythonize(ext))