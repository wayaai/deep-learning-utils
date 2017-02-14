import os

from setuptools import find_packages
from setuptools import setup


def read(file_name):
    with open(os.path.join(os.path.dirname(__file__), file_name), 'r') as f:
        return f.readlines()

setup(
    name='deep-learning-utils',
    version='0.0.0',
    description='A clean and general implementation of some common utils and tools required by various deep learning '
                'projects.',
    # long_description=read('README.md'),
    url='https://github.com/wayaai/deep-learning-utils.git',
    author='Michael Dietz',
    keywords='',
    packages=find_packages(exclude=["tests.*", "tests"]))
