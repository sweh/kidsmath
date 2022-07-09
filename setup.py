#!/usr/bin/env python

"""The setup script."""

from setuptools import find_packages, setup

with open('README.md') as readme_file:
    readme = readme_file.read()

with open('CHANGES.rst') as history_file:
    history = history_file.read()

setup(
    author='Sebastian Wehrmann',
    author_email='sebastian@wehrmann.it',
    python_requires='>=3.9',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: German',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
    ],
    description='Zufällige Matheaufgaben für Kinder.',
    install_requires=[
    ],
    entry_points={
        'console_scripts': [
            'kidsmath=kidsmath:run',
        ],
    },
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='kids math',
    name='kidsmath',
    packages=find_packages('src'),
    package_dir={'': 'src'},
    url='https://github.com/sweh/kidsmath',
    version='0.1.0.dev0',
    zip_safe=False,
)
