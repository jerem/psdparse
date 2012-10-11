#!/usr/bin/env python
from distutils.core import setup

setup(
    name = 'psdparser',
    version = '0.1',
    author = 'Jeremy Bethmont',
    author_email = 'jeremy.bethmont@gmail.com',
    url = 'https://github.com/jerem/psdparse',

    description = 'PSD parser',
    long_description = open('README.txt').read(),

    license = 'GPLv2',
    packages = ['psdparse'],
    scripts=['bin/psdparser.py'],
    requires=['PyYAML', 'PIL'],

    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.5',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Multimedia :: Graphics',
        'Topic :: Multimedia :: Graphics :: Viewers',
        'Topic :: Multimedia :: Graphics :: Graphics Conversion',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
