from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT ="-e ."
def get_requirements(file_path: str) -> List[str]:
    """this functionm will return the list of requiremnets"""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        [requirement.replace("\n", " ") for requirement in requirements]
        if HYPEN_E_DOT in requirements :
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="MLproject",
    version="0.0.1",
    author="Nischal",
    author_email="nischal.maharjan1233@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
