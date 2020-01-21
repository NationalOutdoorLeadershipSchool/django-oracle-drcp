#!/usr/bin/env python
from setuptools import find_packages, setup


setup(
    name="django-nols-drcp",
    packages=find_packages(),
    url="https://github.com/NationalOutdoorLeadershipSchool/django-nols-drcp",
    version="1.0.5",
    description="A Django database backend for Oracle with DRCP",
    author="NOLS Developers",
    author_email="developer@nols.edu",
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Framework :: Django",
        "License :: OSI Approved :: BSD License",
        "Development Status :: 3 - Alpha",
        "Operating System :: OS Independent",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "Topic :: Database",
    ],
)
