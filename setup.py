from setuptools import setup, find_packages

setup(
   name='planprogenerator',
   version='1.0',
   description='A simple toolkit to generate planpro files',
   author='OSM@HPI',
   packages=find_packages(),  # would be the same as name
   install_requires=['yaramo @ git+https://github.com/simulate-digital-rail/yaramo.git'],
   setup_requires=['yaramo @ git+https://github.com/simulate-digital-rail/yaramo.git']
)
