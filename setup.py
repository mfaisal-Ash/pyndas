from distutils.core import setup, Extension
import subprocess
subprocess.run(["pandoc","--from=markdown","--to=rst","--output=README","README.md"])

with open("README", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
  name = 'pyndas',
  packages = ['pyndas'],
  version = '0.0.1',
  packages = find_packages(),
  license='MIT',
  description = 'Library ini digunakan untuk memudahkan transformasi data',
  long_description=long_description,
  author = 'MFaidiq',
  author_email = 'faisalsidiq14@gmail.com',
  url = 'https://github.com/mfaisal-Ash/pyndas',
  download_url = '',
  keywords = ['pyndas', 'py-ndas', 'pyd'],
  install_requires=[
          'requests',
	  'lxml',
      ],
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
