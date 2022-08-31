from gettext import install
from setuptools import setup
from typing import List


def get_requirements_list()->List[str]:
    '''
    This function will going to return a list of strings which will contain name for all the libraries specified with requirements.txt
    '''
    with open("requirements.txt","r") as f:
        return f.readlines()

setup(
name="Shipping-cost-prediction",
version="0.0.2",
author="Anindita",
description="This is cover type predictor setup file",
packages=["Supply_Chain"],
install_requires=get_requirements_list()
)

