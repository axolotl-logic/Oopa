from setuptools import find_packages, setup

setup(
    name="oopa",
    version="2.0.1",
    description="A script that dumps stats on a wordlist for password research",
    author="Axolotl-Logic",
    author_email="me@axolotl-logic.io",
    packages=find_packages(),
    scripts=["bin/oopa"],
    install_requires=["prettytable"],
    url="https://www.axolotl-logic.io/",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    license="MIT",
)
