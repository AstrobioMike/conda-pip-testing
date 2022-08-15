import os
import glob
from setuptools import setup, find_packages

# reading README
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

with open(os.path.join(os.path.dirname(__file__), 'README.md')) as readme:
    README = readme.read()

requirements = [req.strip() for req in open('requirements.txt', 'r').readlines()]

setup(
    name = "conda-pip-testing",
    version = "0.1",
    description = "A testing area for me to learn how to better organize my python packages",
    author = "Mike Lee",
    author_email = "Mike.Lee@nasa.gov",
    url = "https://github.com/AstrobioMike/conda-pip-testing",

    packages = find_packages(),
    scripts = [script for script in glob.glob('bin/*')],
    include_package_data = True,
    install_requires = requirements,

    classifiers = [
    "Environment :: Console",
    "Environment :: MacOS X",
    "License :: OSI Approved :: GNU GPLv3 License",
    "Natural Language :: English",
    "Operating System :: POSIX :: Linux",
    "Operating System :: MacOS :: MacOS X",
    "Programming Language :: Python :: 3.9",
    ],
)