from setuptools import setup, find_packages
# from typing import List
setup(
    name='sensor',
    version='0.0.1',
    author='Sambeet Sabat',
    author_email='sambeetsabat17@gmail.com',
    packages=find_packages(),
    install_requires=[
        'pymongo==4.2.0']
)