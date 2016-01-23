import os
from setuptools import setup, find_packages

def read(fname):
    with open(os.path.join(os.path.dirname(__file__), fname)) as f:
        return f.read()

setup(
    name = "multi_distribution_support",
    version = "0.0.1",
    author = "Raja",
    author_email =  "r.rajaravi@gmail.com",
    description = ("An demonstration of how to create code for "
                       "multiple distribution of an operating system."),
    license = "BSD",
    keywords = "multi distribution",
    packages = find_packages('src'),
    package_dir={'': 'src'},
    include_package_data=True,
    long_description =  read('README.md'),
    classifiers = [
        "Programming Language :: Python",
        "Development Status :: 3 - Alpha",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 2.7",
        "Topic :: Software Development",
    ],
    url = '',

)
