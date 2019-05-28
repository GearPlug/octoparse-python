import os

from setuptools import setup


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


setup(name='octoparse-python',
      version='0.1.1',
      description='API wrapper for Octoparse written in Python',
      long_description=read('README.md'),
      long_description_content_type="text/markdown",
      url='https://github.com/GearPlug/octoparse-python',
      author='Miguel Ferrer',
      author_email='ingferrermiguel@gmail.com',
      license='MIT',
      packages=['octoparse'],
      install_requires=[
          'requests',
      ],
      zip_safe=False)
