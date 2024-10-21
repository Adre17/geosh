from setuptools import setup, find_packages, Extension
from Cython.Build import cythonize
import numpy as np

# Define an extension that includes your Cython file
extensions = [
    Extension(
        "geosh.cy_theoretical_dc",  # Update to match the package name
        ["geosh/cy_theoretical_dc.pyx"],  # Cython source file path
        include_dirs=[np.get_include()],  # Include NumPy headers
    )
]

# Setup the package
setup(
    name="geosh",  # The name of the package
    version="0.1.0",  # Version number
    author="Umberto Grechi",
    author_email="umberto.grechi@sofhare.com",
    description="Library and fependency for Geo Utilities Plugin",  # Short description
    long_description=open("README.md").read(),  # Detailed description from README
    long_description_content_type="text/markdown",
    url="https://github.com/Adre17/geosh",  # URL to your repository
    packages=find_packages(),  # Automatically find and include sub-packages
    ext_modules=cythonize(extensions, compiler_directives={'language_level': "3"}),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",  # Minimum required Python version
    install_requires=[  # Dependencies to be installed
        'xlrd',
        'pyproj',
        'numpy',
        'shapely',
        'matplotlib',
        'Pillow',
        'psycopg2',
        'reportlab',
        'segyio',
        'opencv-python',
        'openpyxl',
        'opencv-contrib-python'
    ],
)

