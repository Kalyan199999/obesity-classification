from setuptools import find_packages , setup
from typing import List

def get_requirements_list() -> List[str]:
    """ This function returns a list of requirements from requirements.txt """
    requirements_list = []
    try:

        with open('requirements.txt') as file:
            # read the each line in the file
            lines = file.readlines()

            for line in lines:

                required = line.strip()

                # remove the empty lines and -e . from the list
                if required and required != '-e .':
                    
                    requirements_list.append(required)

    except FileNotFoundError as err:

        print(f"File (requirements.txt) Not found!")

    return requirements_list

setup(
name='Obesity Classification',
version='0.0.1',
author='Kalyan',
author_email='kalyan@gmail.com',
# finds all the packages in the current directory
packages=find_packages(),

# get all the requirements from requirements.txt
install_requires=get_requirements_list(),
description='This is a ML project to predict obesity',
long_description=open('README.md').read(),

)