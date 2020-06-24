from setuptools import setup, find_packages
from os.path import join, dirname


setup(
    name='lr2',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__),
                               'README.txt')).read(),
    author='Dmitry Dankov',
    author_email='12ddankov12@gmail.com',
)
