# import tools
from setuptools import setup, Extension

# For compilation
module = Extension('hola_modulo', sources=['hola_modulo.c'])

# Setup
setup(
    name='HolaMundoCModule',
    version='0.1.0',
    ext_modules=[module]
)
