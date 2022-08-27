from setuptools import setup

setup(
   name='planprogenerator',
   version='1.0',
   description='A simple toolkit to generate planpro files',
   author='OSM@HPI',
   setup_requires=['wheel'],
   packages=['planprogenerator', 'planprogenerator.model', 'planprogenerator.planproxml'],
   dependency_links=['https://github.com/arneboockmeyer/railway-route-generator']
)
