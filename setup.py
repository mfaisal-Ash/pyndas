from setuptools import setup, find_packages

setup(
    name="pyndas",
    version="0.0.1",
    packages=find_packages(),
    install_requires=["pymongo"],
    description="Library for MongoDB data transformation and redundancy removal",
    author="MFaidiq",
    url="https://github.com/mfaisal-Ash/pyndas",
)
