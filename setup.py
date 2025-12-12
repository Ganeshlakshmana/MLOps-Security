from setuptools import setup, find_packages
from typing import List

def get_requirements()-> List[str]:
    """Read the requirements from requirements.txt file."""
    requirements_lst:List[str] = []
    
    try:
        with open('requirements.txt', 'r') as file:
            """ Read lines from requirements.txt and return as a list """
            lines = file.readlines()
            """ reading each lines from requirements.txt and adding to requirements_lst """
            for line in lines:
                requirement=line.strip()
                """ Avoid adding empty lines and spaces"""
                if requirement and requirement!='-e .':
                    requirements_lst.append(requirement)
    except FileNotFoundError:
        print("requirements.txt file not found. No dependencies will be installed.")
    return requirements_lst
# print(get_requirements())

setup(
    name='MLOps_Project',
    version='0.1.0',
    author='Ganesh Lakshmana',
    author_email='gani2001guddi@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements(),
    description='A sample MLOps project setup',
)
    
    