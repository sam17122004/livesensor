from setuptools import setup, find_packages
from typing import List
def get_requirements()->list[str]:
    requirements_list : list[str]= []
    return requirements_list
    
    
    
    
    

 
setup(
    name='sensor',
    version='0.0.1',
    author='Sambeet Sabat',
    author_email='sambeetsabat17@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
)