from setuptools import setup

setup(
   name='Tallest Tree Bot',
   version='0.1',
   description='bot that watches your screen and plays Tallest Tree for you.',
   author='Dave Feinblum',
   author_email='me@dvfeinblum.com',
   install_requires=['keyboard', 'mss', 'numpy', 'opencv-python', 'Pillow'],
)
