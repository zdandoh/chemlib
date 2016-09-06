import os
from setuptools import setup

setup(
    name="chemlib",
    version="0.1.1",
    description="A lightweight library for chemistry",
    author="zdandoh",
    author_email="link.dohi@gmail.com",
    license="MIT",

    packages=["chemlib", os.path.join("chemlib", "part")]
)
