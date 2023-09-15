#!/usr/bin/env python
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

# We use calendar versioning
version = "2023.09.11"

with open("README.md") as readme_file:
    long_description = readme_file.read()

setup(
    name="cookiecutter-vue3-django",
    version=version,
    description=("A Vue3 + Vite template for creating production-ready Django projects quickly."),
    long_description=long_description,
    author="Mike Hoolehan, Daniel Roy Greenfeld",
    author_email="mike@hoolehan.com",
    url="https://github.com/ilikerobots/cookiecutter-django",
    packages=[],
    license="BSD",
    zip_safe=False,
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Framework :: Django :: 4.2",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: Implementation :: CPython",
        "Programming Language :: JavaScript",
        "Topic :: Software Development",
    ],
    keywords=(
        "cookiecutter, vue, vite, Python, projects, project templates, django, "
        "skeleton, scaffolding"
    ),
)
