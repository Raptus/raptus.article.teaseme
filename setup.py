from setuptools import setup, find_packages
import os

version = '1.0a2.dev0'

long_description = (
    open("README.rst").read() + "\n" +
    open(os.path.join("docs", "MANUAL.txt")).read() + "\n" +
    'Contributors\n'
    '============\n'
    + '\n' +
    open('CONTRIBUTORS.txt').read() + "\n" +
    open("CHANGES.txt").read())

setup(name='raptus.article.teaseme',
      version=version,
      description="Provides a responsive teaser component",
      long_description=long_description,
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        ],
      keywords='',
      author='Raptus AG',
      author_email='dev@raptus.com',
      url='http://github.com/Raptus/raptus.article.teaseme',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['raptus', 'raptus.article'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'raptus.backgroundsize',
          'raptus.article.core>2.0b12',
          'raptus.article.teaser',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
