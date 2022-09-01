from setuptools import setup, find_packages

setup(
   name='planprogenerator',
   version='1.0',
   description='A simple toolkit to generate planpro files',
   author='OSM@HPI',
   setup_requires=['wheel'],
   packages=find_packages(),
   install_requires=['pyproj'],
   dependency_links=['https://github.com/arneboockmeyer/railway-route-generator']
)
