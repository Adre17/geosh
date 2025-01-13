# setup.py
from setuptools import setup
from Cython.Build import cythonize
import numpy as np

setup(
    ext_modules=cythonize("cy_theoretical_dc.pyx",
                           build_dir='build',
                           compiler_directives={'language_level': "3"}),
    include_dirs=[np.get_include()],  # Include NumPy headers
    script_args=['build_ext', '--inplace'],
)

