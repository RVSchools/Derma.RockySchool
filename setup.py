from setuptools import setup, find_packages
import os

version = '1.0.1'

setup(name='Derma.RockySchool',
      version=version,
      description="An installable theme for Plone 3.0",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from http://www.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Programming Language :: Python",
        "Topic :: Software Development :: Libraries :: Python Modules",
        ],
      keywords='web zope plone theme',
      author='Vurtur',
      author_email='info@vurtur.com',
      url='http://www.vurtur.com',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['Derma'],
      include_package_data=True,
      zip_safe=True,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-
      """,
      )
