from setuptools import setup, find_packages

setup(
    name='pyndas',
    version='0.1',
    packages=['pyndas'],  # Pastikan ini sesuai dengan direktori yang ada
    install_requires=['pymongo'],  # Tambahkan dependencies yang diperlukan
    description='Library for MongoDB data transformation and redundancy removal',
    author='Mfaidiq',
    url="https://github.com/mfaisal-Ash/pyndas",
    download_url = '',  
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
    python_requires='>=3.8',
    python_requires='>=3.10',
    python_requires='>=3.12',
)
