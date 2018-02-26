from setuptools import setup, find_packages
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'readme.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='selenium_page_elements',
    version='0.1.6',
    description='A small library for simplifying page objects.',
    long_description=long_description,

    url='https://github.com/jenterkin/selenium-page-elements',

    author='Jordan Enterkin',
    author_email='jordan.a.enterkin@gmail.com',

    license='MIT',

    # See https://pypi.python.org/pypi?%3Aaction=list_classifiers
    classifiers=[
        'Development Status :: 3 - Alpha',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Testing',

        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3.6',
    ],

    keywords='selenium page objects',

    packages=['page_elements'],

    install_requires=['selenium>=3.4.0'],
    extras_require={
        'test': ['coverage>=4.3.4', 'docker>=2.2.1', 'pytest>=3.0.7']
    }
)
