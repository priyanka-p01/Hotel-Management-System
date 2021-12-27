from setuptools import setup, find_packages
from os import path


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name = 'Hotel-Management-System',
    version = '1.0.0',
    license='MIT License',
    description = 'Python-based Hotel Management System that uses text to speech library to welcome the patrons. It can be also used to auto-generate the bills for the orders placed by customers',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    include_package_data = True,
    install_requires = ['pyttsx3'],
)