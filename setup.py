# -*- encoding: utf-8 -*-
from setuptools import find_packages
from setuptools import setup

install_requires = [
    'django==1.10.5',
    'morfdict==0.3.7',

    'baelfire==0.3.2',
    'bael.project==0.2.4',
    'pytest==3.0.6',
    'pytest-django==3.1.2',
    'ipython==5.1.0',
    'ipdb==0.10.1',
    'freezegun==0.3.8',
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
            'console_scripts': (
                'serv = baelszeol.cmd:runserver',
                'shell = baelszeol.cmd:shell',
                'manage = baelszeol.cmd:manage',
                'tests = baelszeol.cmd:tests',
                'testscov = baelszeol.cmd:coverage',
            )
        }
    )
