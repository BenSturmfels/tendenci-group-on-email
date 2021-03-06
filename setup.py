#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""The setup script."""

from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

# with open('HISTORY.rst') as history_file:
#     history = history_file.read()

requirements = [ ]

# setup_requirements = ['pytest-runner', ]

# test_requirements = ['pytest', ]

setup(
    author="Ben Sturmfels",
    author_email='ben@sturm.com.au',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Natural Language :: English',
        "Programming Language :: Python :: 2",
        'Programming Language :: Python :: 2.7',
        # 'Programming Language :: Python :: 3',
        # 'Programming Language :: Python :: 3.4',
        # 'Programming Language :: Python :: 3.5',
        # 'Programming Language :: Python :: 3.6',
    ],
    description='Apply discounts and permissions to account groups based on email suffix, eg. ".edu."',
    install_requires=requirements,
    license="GNU General Public License v3",
    long_description=readme,
    # long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='tendenci-group-on-email',
    name='tendenci-group-on-email',
    packages=find_packages(),
    # setup_requires=setup_requirements,
    # test_suite='tests',
    # tests_require=test_requirements,
    url='https://github.com/BenSturmfels/tendenci-group-on-email',
    version='0.1.4',
    zip_safe=False,
)
