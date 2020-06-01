"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
https://github.com/pypa/sampleproject
https://github.com/navdeep-G/setup.py

https://docs.python.org/2/distutils/setupscript.html

$ python setup.py build && python setup.py install
"""

from setuptools import setup, find_packages
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file.
#
with open(path.join(here, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='scrapy-selenium',
    version='0.0.8',
    description='Using Selenium (Remote) with Scrapy',
    long_description=long_description,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3 :: Only',
    ],
    packages=['scrapy_selenium'],
    python_requires='>=3.5, <4',
    extras_require={
    },
    package_data={
    },
    data_files=[],
    entry_points={
    },
    project_urls={
    },
)