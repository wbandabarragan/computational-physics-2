# Import the libraries needed for the set up

from setuptools import find_packages, setup

setup(name = "mdensity",
      description = "This produces density maps base on user inputs",
      author="WEBB", 
      license = "BSD",
      version = "1.0",
      packages = find_packages(),
      install_requires = ["numpy", "matplotlib", "scipy"])
