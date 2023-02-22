from setuptools import setup, find_packages

setup(name='mymodule',
      description='test module for PHY 546',
      url='https://github.com/sbu-python-class/mymodule',
      author='Michael Zingale',
      author_email='michael.zingale@stonybrook.edu',
      license='BSD',
      packages=find_packages(),
      install_requires=['numpy', 'matplotlib'])
