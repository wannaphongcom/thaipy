#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from setuptools import setup
from setuptools import find_packages

requirements = [
    # TODO: put package requirements here
]
readme="""Write Python 3 language in thai lang."""

setup(
    name='thaipy',
    version='0.0.2',
    description="Write Python 3 language in thai lang.",
    long_description=readme,# + '\n\n' + history,
    author="Wannaphong Phatthiyaphaibun",
    author_email='wannaphong@yahoo.com',
    url='https://github.com/wannaphongcom/thaipy',
    packages=['example','run'],
    package_data={'example':['love.thpy','test.thpy']},
    include_package_data=True,
    install_requires=requirements,
    license="Apache Software License 2.0",
    zip_safe=False,
    entry_points={
		'console_scripts': ['thaipy = run.thaipy:main']
    },
    keywords='thaipy',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Education',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Natural Language :: Thai',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Code Generators',
        'Programming Language :: Python :: 3',
    ],
    test_suite='tests',
)