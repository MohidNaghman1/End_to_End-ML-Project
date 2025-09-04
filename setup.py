from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path:str) -> List[str]:
    '''This function will return the list of requirements'''
    with open(file_path) as f:
        requirements = f.read().splitlines()

    # Agar '-e .' line ho to usko ignore kar do
    requirements = [req for req in requirements if req.strip() != "-e ."]

    return requirements

setup(
    name='ML_Project',
    version='0.0.1',
    author='Mohid',
    author_email='mohidnaghman315@gmail.com', 
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)