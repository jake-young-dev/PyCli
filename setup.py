from setuptools import setup

setup(
   name='PyCli',
   version='1.0',
   description='A Python API Client',
   author='jake-young-dev',
   author_email='',
   packages=['PyCli'],  #same as name
   install_requires=[], #external packages as dependencies
   scripts=["client.py"]
)