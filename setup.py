from setuptools import setup, find_packages
from setuptools.command import sdist

setup (
    name = 'weblyzard_api',
    version = '0.3.1',
    description= ' Web services for weblyzard',
    author = 'Heinz-Peter Lang and Albert Weichselbraun',
    author_email = 'lang@weblyzard.com',
    packages = find_packages('src'),
    package_dir = {'': 'src'},
    install_requires = ['eWRT>=0.7.10', ],
    scripts = ['src/weblyzard_api/client/recognize/wl_upload_repository.py',]
)
