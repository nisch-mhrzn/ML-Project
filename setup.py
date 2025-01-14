from setuptools import find_packages, setup
from typing import List

HYPHEN_E_DOT = "-e ."

def get_requirements(file_path: str) -> List[str]:
    """This function will return the list of requirements."""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        # Strip newline characters
        requirements = [requirement.strip() for requirement in requirements]
        # Remove '-e .' if present
        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    return requirements

setup(
    name="MLproject",
    version="0.0.1",
    author="Nischal",
    author_email="nischal.maharjan1233@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
