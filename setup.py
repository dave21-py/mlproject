from setuptools import find_packages, setup
from typing import List;
## builds __init__.

def get_requirements(file_path:str) -> List[str]:
    '''
    This function returns a list
    '''
    requirements = []
    HYPHEN_E_DOT = '-e .'
    with open(file_path) as f:
        requirements = f.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="ml-project",
    version="0.001",
    author="David",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')

)