# -*- coding: utf-8 -*-
"""
This module contains the tool of uqmc.theme
"""
import os
from setuptools import setup, find_packages

version = '0.1'

setup(name='uqmc.theme',
      version=version,
      description="",
      long_description="",
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        'Framework :: Plone',
        'Intended Audience :: Developers',
        ],
      keywords='',
      author='Alex Stevens',
      author_email='alexander.stevens@uqconnect.edu.au',
      url='https://github.com/AlexStevens/uqmc.theme/',
      license='gpl',
      packages=find_packages('src'),
      package_dir = {'': 'src'},
      namespace_packages=['uqmc'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
            'setuptools',
            'plone.app.theming',
            'plone.app.jquery',
            'five.grok',
        ],
      entry_points="""
      # -*- entry_points -*-
      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
