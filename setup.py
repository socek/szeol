# -*- encoding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

install_requires = [
    'django==1.10.5',
    'morfdict==0.3.7',
]


if __name__ == '__main__':
    setup(
        name='szeol',
        version='0.1',
        description='Szeol CRM',
        url='https://github.com/socek/szeol',
        license='Apache License 2.0',
        packages=find_packages('src'),
        package_dir={'': 'src'},
        install_requires=install_requires,
        entry_points={
        }
    )
