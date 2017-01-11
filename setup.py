#!/usr/bin/env python

from setuptools import setup

setup(name = "coverage",
      version = "1",
      description = "Python package for calculating a gray level for text.",
      author = "Erik van Blokland",
      author_email = "erik@letterror.com",
      url = "https://github.com/LettError/coverage",
      license = "MIT",
      packages = [
              "coverage",
      ],
      package_dir = {"":"Lib"},
)
