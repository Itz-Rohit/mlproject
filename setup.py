from setuptools import setup, find_packages
from typing import List

def get_requirements(file_path: str) -> List[str]:  # ✅ Fixed the annotation
    '''
    This function will return the list of requirements
    '''
    requirements = []
    with open(file_path, encoding='utf-8') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]  # ✅ Used strip() instead of replace
        if '-e .' in requirements:
            requirements.remove('-e .')
    return requirements

setup(
    name='mlproject',  
    version='0.0.1',  
    author='Rohit Kumar',  
    author_email='srohitkumar0007@gmail.com',  
    packages=find_packages(),  
    install_requires=get_requirements('requirements.txt'),  
)
