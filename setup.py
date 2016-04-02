__author__ = 'danleyb2<ndieksman@gmail.com>'
import os
from setuptools import setup
import setuptools

with open(os.path.join(os.path.dirname(__file__), 'README.rst')) as readme:
    README = readme.read()

# allow setup.py to be run from any path
os.chdir(os.path.normpath(os.path.join(os.path.abspath(__file__), os.pardir)))

setup(
        name='django-pa',
        version='0.1',
        packages=setuptools.find_packages(),
        include_package_data=True,
        zip_safe=False,
        license='GNU License',
        description='Django app that act as your restFull personal assistant',
        long_description=README,
        url='https://www.example.com/',
        author='danleyb2',
        author_email='ndieksman@gmail.com',
        classifiers=[
            'Development Status :: 0.01 - Beta ',
            'Environment :: Web Environment',
            'Framework :: Django',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: BSD License',
            'Operating System :: OS Independent',
            'Programming Language :: Python',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.2',
            'Programming Language :: Python :: 3.4',
            'Topic :: Internet :: WWW/HTTP',
            'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        ],
)