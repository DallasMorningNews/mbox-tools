# Imports from python.  # NOQA
import os
from setuptools import find_packages
from setuptools import setup


REPO_URL = 'https://github.com/DallasMorningNews/mbox-tools/'

PYPI_VERSION = '0.3.0'

DESCRIPTION = 'Simple tools for summarizing .mbox email archives.'


# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
    name='mbox-tools',
    version=PYPI_VERSION,
    packages=find_packages(),
    include_package_data=True,
    license='AGPLv3',
    description=DESCRIPTION,
    long_description=DESCRIPTION,
    url=REPO_URL,
    download_url='{repo_url}archive/{version}.tar.gz'.format(**{
        'repo_url': REPO_URL,
        'version': PYPI_VERSION,
    }),
    author='Allan James Vestal, The Dallas Morning News',
    author_email='newsapps@dallasnews.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU Affero General Public License v3',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Communications :: Email',
    ],
    install_requires=[
        'mailbox~=0.4',
    ],
)
