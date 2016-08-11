"""
Install the package containing the SPARQL kernel for Jupyter.
To actually use the kernel it needs to be installed into Jupyter afterwards.
"""

from __future__ import print_function
import os
import os.path
import sys

from setuptools import setup

from sparqlkernel.constants import __version__, LANGUAGE, DISPLAY_NAME

PKGNAME = 'sparqlkernel'

setup_args = dict (
    name=PKGNAME,
    version=__version__,
    description= 'A Jupyter kernel for SPARQL queries',
    long_description=
'''This module installs a Jupyter kernel for SPARQL. It allows sending queries
to an SPARQL endpoint and fetching & presenting the results in a notebook.
It is implemented as a Jupyter wrapper kernel, by using the Python 
SPARQLWrapper & rdflib packages''',
    license='3-clause BSD license',
    url='https://github.com/paulovn/sparql-kernel',
    author='Paulo Villegas',
    author_email='paulo.vllgs@gmail.com',

    packages=[ PKGNAME ],
    install_requires = [ 'setuptools',
                         'ipykernel >= 4.0',
                         'traitlets',
                         'rdflib',
                         'pygments',
                         'SPARQLWrapper', ],

    entry_points = { 
        'console_scripts': 
        [ 'jupyter-sparqlkernel = sparqlkernel.__main__:main'],
        'pygments.lexers' :
        ['sparql_with_magic = sparqlkernel.pygments_sparql:SparqlLexerMagics']
    },
    package_data = { 
        PKGNAME: [ 'resources/logo-*x*.png', 
                   'resources/*.css' ],
    },
    include_package_data = True,

    classifiers = [
          'Framework :: IPython',
          'Programming Language :: Python :: 2.7',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.4',
          'License :: OSI Approved :: BSD License',
          'Development Status :: 4 - Beta',
          'Topic :: Database :: Front-Ends',
          'Topic :: System :: Shells',
      ],      
  )


if __name__ == '__main__':
    setup( **setup_args )
