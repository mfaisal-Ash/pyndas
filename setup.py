from distutils.core import setup
import subprocess
subprocess.run(["pandoc","--from=markdown","--to=rst","--output=README","README.md"])

with open("README", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='pyndas',
    version='0.0.3',
    packages=['pyndas'],
    install_requires=['pymongo', 'time'],  # Tambahkan dependencies yang diperlukan
    author='Mfaidiq',
    author_email='faisalsidiq14@gmail.com',
    description='Library for MongoDB data transformation and redundancy removal',
    long_description=long_description,
    url="https://github.com/mfaisal-Ash/pyndas",
    download_url='',
    keywords = ['pyndas','py-ndas'],  
    classifiers=[
    'Development Status :: 3 - Alpha',
    'Intended Audience :: Developers',
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Programming Language :: Python :: 3.8',
    'Programming Language :: Python :: 3.9',
    'Programming Language :: Python :: 3.10',
    'Programming Language :: Python :: 3.11',
    'Programming Language :: Python :: 3.12',
    ],
)
