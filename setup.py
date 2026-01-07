#!/usr/bin/env python
# -*- coding: UTF-8 -*-

"""ycnbc - CNBC data downloader"""

from setuptools import setup, find_packages
import io
from os import path

# --- get version ---
version = "unknown"
with open("ycnbc/version.py") as f:
    line = f.read().strip()
    version = line.replace("version = ", "").replace('"', '')
# --- /get version ---

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with io.open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='ycnbc',
    version=version,
    description='Download data from CNBC!',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/asepscareer/ycnbc',
    author='Asep Saputra',
    author_email='asepscareer@gmail.com',
    license='Apache',
    classifiers=[
        'License :: OSI Approved :: Apache Software License',
        'Development Status :: 5 - Production/Stable',
        'Operating System :: OS Independent',
        'Intended Audience :: Developers',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content :: News/Diary',
        'Topic :: Office/Business :: Financial',
        'Topic :: Office/Business :: Financial :: Investment',
        'Topic :: Scientific/Engineering :: Interface Engine/Protocol Translator',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
    ],
    platforms=['any'],
    keywords='scrape news, cnbc library, cnbc python, cnbc api',
    packages=find_packages(exclude=['contrib', 'docs', 'tests', 'examples']),
    install_requires=['curl-cffi>=0.5.9', 'lxml>=4.9.3',
                      'cssselect>=1.2.0', 'mypy', 'tenacity'],
    entry_points={
        'console_scripts': [
            # 'sample=sample:main',
        ],
    },
)

print(
    """
    NOTE: ycnbc is not affiliated, endorsed, or vetted by CNBC.
    You should refer to CNBC!'s terms of use for details on your rights to use the actual data downloaded.
    """
)
